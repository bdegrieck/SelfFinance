import os
import subprocess

import click
from dotenv import load_dotenv

from src.database.entrypoint import create_db

load_dotenv()
PG_CTL = os.getenv("POSTGRES_ROOT_PATH_MAC")
PG_DATA = os.getenv("POSTGRES_DATA_DIRECTORY_MAC")


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
        subprocess.run([PG_CTL, "stop", "-D", PG_DATA, "-m", "fast"], check=True)
    except subprocess.CalledProcessError:
        pass

    # Start fresh
    subprocess.run([PG_CTL, "start", "-D", PG_DATA], check=True)
    click.echo("PostgreSQL started.")


@cli.command(name="stop-postgres")
def cli_stop_postgres():
    """
    Stop the PostgreSQL service.
    """
    subprocess.run([PG_CTL, "stop", "-D", PG_DATA, "-m", "fast"], check=True)
    click.echo("PostgreSQL stopped.")


@cli.command(name="start-engine")
def cli_start_engine():
    """
    Ensure PostgreSQL is running and then connect the SQLAlchemy engine.
    """
    # Start Postgres if not already
    ctx = click.get_current_context()
    ctx.invoke(cli_start_postgres)

    engine = create_db()
    try:
        with engine.connect():
            click.echo("Connected to database via SQLAlchemy engine.")
    except Exception as e:
        click.echo(f"Failed to connect to database: {e}", err=True)


if __name__ == "__main__":
    cli()
