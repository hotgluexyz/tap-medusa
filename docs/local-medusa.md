# Run Medusa locally

Requires Node.js 22.12+ (22 LTS), npm, Git, and Docker. Run the steps below
from the repository root. The generated app lives in `.secrets/`, which Git ignores.

## 1. Start PostgreSQL 17

```bash
docker run --detach --name tap-medusa-postgres \
  --publish 127.0.0.1:5433:5432 \
  --env POSTGRES_USER=medusa \
  --env POSTGRES_PASSWORD=medusa_local \
  --env POSTGRES_DB=tap_medusa \
  --volume tap-medusa-postgres-data:/var/lib/postgresql/data \
  postgres:17
```

Allow a few seconds for PostgreSQL to start. These credentials are for local
development only.

## 2. Create Medusa (first run only)

```bash
mkdir -p .secrets
npx create-medusa-app@latest tap-medusa-store \
  --directory-path .secrets --use-npm --no-browser \
  --db-url 'postgres://medusa:medusa_local@127.0.0.1:5433/tap_medusa'
```

Decline the Next.js storefront if prompted. If the installer starts a server,
stop it with Ctrl+C before continuing. Skip this step if the app already exists.

## 3. Create an admin user (first run only)

```bash
(cd .secrets/tap-medusa-store/apps/backend && \
  npx medusa user -e admin@example.com -p 'local-medusa-password')
```

Skip this step if you already have an admin user.

## 4. Start Medusa

```bash
cd .secrets/tap-medusa-store/apps/backend
npm run dev
```

Open <http://localhost:9000/app> and log in with the credentials above.
Keep the terminal open while using Medusa; Ctrl+C stops it.

On subsequent runs, use `docker start tap-medusa-postgres` and repeat step 4
from the repository root. To stop the database, run `docker stop tap-medusa-postgres`.

## 5. Configure the tap

In a separate terminal at the repository root, create the configuration directory:

```bash
mkdir -p .secrets/local-medusa
```

Create `.secrets/local-medusa/config.json` with:

```json
{
  "base_url": "http://localhost:9000",
  "email": "admin@example.com",
  "password": "local-medusa-password",
  "medusa_v2": true
}
```

See the [Medusa installation guide](https://docs.medusajs.com/learn/installation)
for more details.
