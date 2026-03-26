# Knowledge Base — TechCorp Internal Support

**Version:** 2.4.1  
**Last Updated:** 2024-03-15  
**Owner:** Platform Engineering Team  
**Classification:** Internal Use Only

---

## Table of Contents

1. [Product Overview](#product-overview)
2. [Authentication & Access](#authentication--access)
3. [API Reference](#api-reference)
4. [Troubleshooting](#troubleshooting)
5. [Billing & Subscriptions](#billing--subscriptions)
6. [Integrations](#integrations)
7. [FAQs](#faqs)
8. [Escalation Matrix](#escalation-matrix)

---

## 1. Product Overview

### What is TechCorp Platform?

TechCorp Platform is a cloud-based SaaS solution that enables teams to manage, monitor, and automate their data pipelines. It supports real-time data ingestion, transformation, and delivery across 50+ connectors.

### Key Features

- **Real-time streaming** — Process up to 10M events/second per workspace
- **No-code pipeline builder** — Drag-and-drop interface for non-technical users
- **Data lineage tracking** — Full audit trail from source to destination
- **Role-based access control (RBAC)** — Granular permissions at workspace, pipeline, and field level
- **99.95% SLA uptime** — Backed by multi-region redundancy

### Supported Tiers

| Tier | Users | Pipelines | Events/month | Support |
|------|-------|-----------|--------------|---------|
| Starter | Up to 5 | 10 | 1M | Email only |
| Growth | Up to 25 | 50 | 10M | Email + Chat |
| Business | Up to 100 | Unlimited | 100M | 24/7 Priority |
| Enterprise | Unlimited | Unlimited | Custom | Dedicated CSM |

---

## 2. Authentication & Access

### Single Sign-On (SSO)

TechCorp supports SSO via:
- **SAML 2.0** — Compatible with Okta, Azure AD, OneLogin
- **OAuth 2.0** — Google Workspace, GitHub
- **LDAP/Active Directory** — Enterprise tier only

To enable SSO:
1. Navigate to **Settings → Security → SSO Configuration**
2. Download the Service Provider metadata XML
3. Upload to your Identity Provider (IdP)
4. Enter the IdP metadata URL in TechCorp settings
5. Click **Test Connection** before activating

> ⚠️ **Note:** SSO enforcement disables username/password login for all users in the org. Ensure at least one backup admin account exists before enabling.

### API Token Management

- Tokens are scoped to **workspace** or **organization** level
- Maximum of **20 active tokens** per user
- Tokens expire after **90 days** by default (configurable by admin)
- All token usage is logged under **Audit Logs → API Activity**

**Token Permissions:**

| Permission | Read | Write | Admin |
|------------|------|-------|-------|
| Pipelines | ✓ | ✓ | ✓ |
| Connectors | ✓ | ✗ | ✓ |
| Users | ✓ | ✗ | ✓ |
| Billing | ✗ | ✗ | ✓ |

### Password Policy

- Minimum 12 characters
- Must include: uppercase, lowercase, number, special character
- Cannot reuse last 5 passwords
- Forced rotation every 180 days for Business/Enterprise

---

## 3. API Reference

### Base URL

```
https://api.techcorp.io/v2
```

### Authentication Header

```http
Authorization: Bearer <your_api_token>
Content-Type: application/json
```

### Endpoints

#### GET /pipelines
Returns all pipelines in the authenticated workspace.

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by: `active`, `paused`, `failed` |
| limit | integer | No | Default: 20, Max: 100 |
| offset | integer | No | Pagination offset |

**Sample Response:**
```json
{
  "data": [
    {
      "id": "pipe_a1b2c3",
      "name": "Salesforce → BigQuery Sync",
      "status": "active",
      "created_at": "2024-01-10T08:00:00Z",
      "last_run": "2024-03-15T14:32:00Z",
      "events_processed": 1482930
    }
  ],
  "total": 1,
  "limit": 20,
  "offset": 0
}
```

#### POST /pipelines
Creates a new pipeline.

**Request Body:**
```json
{
  "name": "My Pipeline",
  "source_id": "conn_xyz123",
  "destination_id": "conn_abc456",
  "schedule": "0 * * * *",
  "transform": "SELECT * FROM events WHERE type = 'click'"
}
```

#### DELETE /pipelines/{pipeline_id}
Permanently deletes a pipeline. This action **cannot be undone**.

---

### Rate Limits

| Tier | Requests/min | Burst |
|------|-------------|-------|
| Starter | 60 | 100 |
| Growth | 300 | 500 |
| Business | 1000 | 2000 |
| Enterprise | Custom | Custom |

Rate limit headers are returned with every response:
```
X-RateLimit-Limit: 300
X-RateLimit-Remaining: 247
X-RateLimit-Reset: 1710512400
```

---

## 4. Troubleshooting

### Common Errors

#### ERR_CONNECTOR_TIMEOUT (504)
**Cause:** Source or destination connector did not respond within 30 seconds.  
**Fix:**
1. Check connector credentials under **Connectors → Settings**
2. Verify the source service is reachable from your network
3. Increase timeout setting: **Pipeline Settings → Advanced → Timeout**
4. If using VPC peering, verify security group rules allow outbound on port 443

---

#### ERR_SCHEMA_MISMATCH (422)
**Cause:** Incoming data schema doesn't match the expected destination schema.  
**Fix:**
1. Go to **Pipeline → Schema → Auto-detect**
2. Run a manual schema refresh
3. If the destination table was altered externally, re-sync the schema
4. Enable **Flexible Mode** to allow schema drift (not recommended for production)

---

#### ERR_AUTH_EXPIRED (401)
**Cause:** API token or SSO session has expired.  
**Fix:**
1. Regenerate your API token under **Settings → API Tokens**
2. For SSO issues, contact your IdP admin to check session duration settings
3. Check if token rotation policy was recently changed by an org admin

---

#### Pipeline Stuck in "Running" State
**Cause:** Long-running job or deadlock in transformation layer.  
**Steps:**
1. Navigate to **Pipeline → Logs → Live Tail**
2. Check for repeated retry attempts (indicates upstream issue)
3. Force-stop the pipeline via **Actions → Force Stop**
4. If the pipeline doesn't stop within 5 minutes, contact support with the Pipeline ID

---

### Performance Optimization Tips

- Use **incremental sync** instead of full refresh where possible — reduces data transfer by up to 80%
- Schedule heavy pipelines during **off-peak hours** (02:00–06:00 UTC)
- Enable **columnar compression** on BigQuery and Snowflake destinations
- Avoid `SELECT *` in transformations — specify required columns explicitly
- Use **batch mode** for pipelines processing >500K events to reduce API overhead

---

## 5. Billing & Subscriptions

### Billing Cycle

- All plans are billed **monthly** or **annually** (15% discount for annual)
- Billing date is set on the day of initial subscription
- Invoices are emailed to the billing contact and available under **Settings → Billing → Invoices**

### Overage Policy

If you exceed your monthly event limit:

| Tier | Overage Rate |
|------|-------------|
| Starter | $0.0008 per 1,000 events |
| Growth | $0.0005 per 1,000 events |
| Business | $0.0003 per 1,000 events |

> Overages are billed at the end of the billing cycle. You can set **usage alerts** at 80% and 100% of your limit under **Settings → Billing → Alerts**.

### Cancellation Policy

- Cancel anytime — no lock-in for monthly plans
- Annual plans: cancel within **14 days** for a full refund; pro-rated refund after 14 days
- Data is retained for **30 days** post-cancellation, then permanently deleted
- Export all data before cancellation via **Settings → Data Export**

---

## 6. Integrations

### Available Native Connectors (50+)

**Data Warehouses:**
Snowflake, BigQuery, Redshift, Databricks, Azure Synapse

**CRM & Sales:**
Salesforce, HubSpot, Pipedrive, Zoho CRM

**Marketing:**
Marketo, Mailchimp, Klaviyo, Braze, Iterable

**Databases:**
PostgreSQL, MySQL, MongoDB, DynamoDB, Cassandra

**File Storage:**
Amazon S3, Google Cloud Storage, Azure Blob, SFTP

**Communication:**
Slack, Microsoft Teams, Zendesk, Intercom

### Webhook Setup

To receive real-time pipeline event notifications:

1. Go to **Settings → Webhooks → Add Endpoint**
2. Enter your endpoint URL (must be HTTPS)
3. Select events to subscribe to:
   - `pipeline.run.success`
   - `pipeline.run.failed`
   - `pipeline.paused`
   - `connector.disconnected`
4. Copy the **Signing Secret** and validate payloads on your server
5. Test with **Send Test Event**

**Webhook Payload Example:**
```json
{
  "event": "pipeline.run.failed",
  "timestamp": "2024-03-15T14:32:00Z",
  "pipeline_id": "pipe_a1b2c3",
  "pipeline_name": "Salesforce → BigQuery Sync",
  "error": "ERR_CONNECTOR_TIMEOUT",
  "retry_count": 3
}
```

---

## 7. FAQs

**Q: Can I migrate data from a competitor platform?**  
A: Yes. TechCorp offers a free **Migration Assist** service for Business and Enterprise customers. Contact your CSM or email migrations@techcorp.io.

**Q: Does TechCorp support HIPAA compliance?**  
A: Yes, for Enterprise tier customers. A Business Associate Agreement (BAA) must be signed before processing PHI. Contact legal@techcorp.io.

**Q: What happens to my data if TechCorp has an outage?**  
A: Events are buffered in a durable queue for up to 24 hours. Once service resumes, buffered events are automatically replayed in order. No data is lost during outages within this window.

**Q: Can I run TechCorp on-premises?**  
A: TechCorp offers a **Private Cloud** deployment option for Enterprise customers. This requires a minimum 12-month commitment. Contact sales@techcorp.io.

**Q: How do I add a new team member?**  
A: Go to **Settings → Team → Invite Member**. Enter their email and assign a role. They'll receive an invite valid for 48 hours. Seats are consumed upon acceptance.

**Q: Is there a sandbox/test environment?**  
A: Yes. Every workspace includes a **Sandbox mode** toggle. Pipelines in sandbox mode do not write to destinations and do not count toward your event quota.

---

## 8. Escalation Matrix

| Issue Type | First Contact | Escalation | SLA |
|------------|--------------|------------|-----|
| Billing dispute | billing@techcorp.io | finance-escalations@techcorp.io | 2 business days |
| Technical bug | support@techcorp.io | engineering-oncall@techcorp.io | 4 hours (Business+) |
| Data loss / corruption | support@techcorp.io | **P0 Hotline: +1-800-555-0199** | 1 hour |
| Security incident | security@techcorp.io | ciso@techcorp.io | 30 minutes |
| Account access locked | support@techcorp.io | identity-ops@techcorp.io | 1 hour |

### Support Hours

| Tier | Hours | Channels |
|------|-------|---------|
| Starter | Mon–Fri, 9am–5pm EST | Email |
| Growth | Mon–Fri, 9am–9pm EST | Email, Chat |
| Business | 24/7 | Email, Chat, Phone |
| Enterprise | 24/7 + Dedicated CSM | All channels + Slack Connect |

---

*For the latest updates to this document, visit the internal wiki at wiki.techcorp.internal/kb or contact the Platform Engineering team on Slack at #platform-support.*
