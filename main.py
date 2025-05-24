import click

from src.database.entrypoint import get_engine


@click.group()
def cli():
    pass


@click.command(name="start-engine")
def connect():
    engine = get_engine()
    with engine.connect():
        click.echo(message="Connected to database")


cli.add_command(cmd=connect, name="start-engine")


if __name__ == "__main__":
    cli()
