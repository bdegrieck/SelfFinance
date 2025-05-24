# SelfFinance

This project uses SQLAlchemy to connect to a Postgres database.

## Configuration

Connection settings are read from environment variables:

- `DB_USER` – database user (default `postgres`)
- `DB_PASSWORD` – user's password
- `DB_HOST` – database host (default `localhost`)
- `DB_PORT` – database port (default `5432`)
- `DB_NAME` – database name (default `postgres`)

Set these variables before running the application.

## Usage

Install the dependencies from `requirements.txt` and use the CLI to test the
database connection:

```bash
python main.py connect
```

