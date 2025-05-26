import subprocess
import os
import click
from dotenv import load_dotenv
from sqlalchemy import text

from src.database.entrypoint import get_engine

load_dotenv()
POSTGRES_ROOT_PATH = os.getenv("POSTGRES_ROOT_PATH")
POSTGRES_VERSION = os.getenv("POSTGRES_VERSION")

ROOT_PATH = os.path.join(POSTGRES_ROOT_PATH, POSTGRES_VERSION)
DATA_DIR = os.path.join(ROOT_PATH, "data")
PG_CTL = os.path.join(ROOT_PATH, "bin", "pg_ctl.exe")


@click.group()
def cli():
    """
    Management commands for the PostgreSQL service and engine.
    """
    pass


@cli.command(name="start-postgres")
def cli_start_postgres():
    """
    Stop any running instance, then start the PostgreSQL service.
    """
    # Stop existing instance if any (ignore errors)
    try:
        subprocess.run([PG_CTL, "stop", "-D", DATA_DIR, "-m", "fast"], check=True)
    except subprocess.CalledProcessError:
        pass

    # Start fresh
    subprocess.run([PG_CTL, "start", "-D", DATA_DIR], check=True)
    click.echo("PostgreSQL started.")


@cli.command(name="stop-postgres")
def cli_stop_postgres():
    """
    Stop the PostgreSQL service.
    """
    subprocess.run([PG_CTL, "stop", "-D", DATA_DIR, "-m", "fast"], check=True)
    click.echo("PostgreSQL stopped.")


@cli.command(name="start-engine")
def cli_start_engine():
    """
    Ensure PostgreSQL is running and then connect the SQLAlchemy engine.
    """
    # Start Postgres if not already
    ctx = click.get_current_context()
    ctx.invoke(cli_stop_postgres)
    ctx.invoke(cli_start_postgres)

    engine = get_engine()
    try:
        with engine.connect():
            click.echo("Connected to database via SQLAlchemy engine.")
    except Exception as e:
        click.echo(f"Failed to connect to database: {e}", err=True)


if __name__ == "__main__":
    cli()
