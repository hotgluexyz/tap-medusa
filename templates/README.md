# tap-medusa Configuration

This document describes the configuration options for the tap-medusa Singer tap, which extracts data from a Medusa e-commerce backend.

## Configuration options

### Connection

#### `base_url` (string, required)
The base URL of your Medusa backend (admin API). Trailing slashes are stripped automatically.
- **Example**: `"https://your-medusa-store.com"` or `"https://api.medusa.example.com/admin"`

### Authentication

Either API key or email/password must be provided.

#### `api_key` (string, optional)
Medusa access token for API key authentication. When set, requests use the `x-medusa-access-token` header instead of email/password login.
- **Example**: `"ntn_xxxxxxxxxxxxxxxxxxxxxxxx"`

#### `email` (string, optional)
Admin email for email/password authentication. Required when not using `api_key`.
- **Example**: `"admin@example.com"`

#### `password` (string, optional)
Admin password for email/password authentication. Required when not using `api_key`.
- **Example**: `"xxxxxxxxxxxxxxxx"`

### API behavior

#### `medusa_v2` (boolean, optional)
Use Medusa v2 API schemas when `true`, v1 schemas when `false`.
- **Default**: `false`
- **Example**: `true` or `false`

#### `user_agent` (string, optional)
Custom User-Agent string sent in HTTP requests.
- **Example**: `"tap-medusa/0.0.1"`

### Incremental sync

#### `start_date` (string, optional)
ISO 8601 datetime used to filter records for incremental syncs. Only records updated after this date are synced. Used when streams have a replication key (e.g. `updated_at`).
- **Example**: `"2024-01-01T00:00:00Z"` or `"2024-06-15"`

---

## Example: minimal config (required only)

Uses email/password authentication and default API version:

```json
{
  "base_url": "https://your-medusa-store.com",
  "email": "admin@example.com",
  "password": "xxxxxxxxxxxxxxxx"
}
```

With API key (no email/password):

```json
{
  "base_url": "https://your-medusa-store.com",
  "api_key": "ntn_xxxxxxxxxxxxxxxxxxxxxxxx"
}
```

---

## Example: full config

```json
{
  "base_url": "https://your-medusa-store.com",
  "email": "admin@example.com",
  "password": "xxxxxxxxxxxxxxxx",
  "api_key": "",
  "medusa_v2": false,
  "user_agent": "tap-medusa/0.0.1",
  "start_date": "2024-01-01T00:00:00Z"
}
```
