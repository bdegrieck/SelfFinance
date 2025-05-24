import click

from src.database.entrypoint import get_engine


@click.group()
def cli() -> None:
    """Command line interface for SelfFinance."""


@cli.command("connect")
def connect_command() -> None:
    """Verify that the database connection works."""
    engine = get_engine()
    with engine.connect():
        click.echo("Successfully connected to the database")


if __name__ == "__main__":
    cli()

