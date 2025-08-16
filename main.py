import os
import platform
import signal
import subprocess

import click
from dotenv import load_dotenv
import uvicorn


from src.api.main import app
from src.database.entrypoint import create_db, clear_database

load_dotenv()

# check if mac
system = platform.system()
if system == "Darwin":
    PG_CTL = os.getenv("POSTGRES_ROOT_PATH_MAC")
    PG_DATA = os.getenv("POSTGRES_DATA_DIRECTORY_MAC")

# check if windows
elif system == "Windows":
    PG_CTL = os.getenv("POSTGRES_ROOT_PATH")
    PG_DATA = os.getenv("POSTGRES_DATA_DIRECTORY")

npm_command = "npm.cmd" if system == "Windows" else "npm"


@click.group()
def cli():
    """
    Management commands for the PostgreSQL service and engine.
    """
    pass


@cli.command(name="start-postgres")
@click.pass_context
def cli_start_postgres(ctx):
    """
    Stop any running instance, then start the PostgreSQL service.
    """
    # Stop existing instance if any (ignore errors)
    ctx.invoke(cli_stop_postgres)
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
    # 1) Try pg_ctl fast shutdown
    try:
        subprocess.run(
            [PG_CTL, "stop", "-D", PG_DATA, "-m", "fast"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        click.echo("pg_ctl stop -m fast succeeded.")
    except subprocess.CalledProcessError:
        click.echo(
            "pg_ctl fast shutdown failed (maybe not started with pg_ctl).",
            err=True,
        )

    # 2) Stop the Homebrew service (if that’s how it was launched)
    pid_file = ""
    if platform.system() == "Darwin":
        subprocess.run(
            ["brew", "services", "stop", "postgresql@14"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        click.echo("brew services stop attempted.")
        pid_file = os.path.join(PG_DATA, "postmaster.pid")
    elif platform.system() == "Windows":
        # adjust the service name if yours is different
        subprocess.run(
            ["net", "stop", "postgresql-x64-17"],
            shell=True,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        click.echo(f"windows services stop attempted.")
        pid_file = os.path.join(PG_DATA, "postmaster.opts")

    if pid_file is None:
        raise ValueError("Error: Operating system must be windows or mac.")

    # 3) Kill any leftover Postgres processes referencing that data dir
    if platform.system() == "Windows":
        subprocess.run(
            ["taskkill", "/F", "/IM", "postgres.exe"],
            shell=True,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        click.echo("taskkill attempted on postgres.exe")
    elif platform.system() == "Darwin":
        pids = []
        if os.path.exists(pid_file):
            with open(pid_file) as f:
                pids.append(int(f.readline().strip()))
        else:
            # fallback: look for any postgres process using your data dir
            out = subprocess.run(
                ["pgrep", "-f", PG_DATA],
                capture_output=True,
                text=True,
                check=False,
            )
            for line in out.stdout.splitlines():
                try:
                    pids.append(int(line))
                except ValueError:
                    pass

        for pid in set(pids):
            try:
                os.kill(pid, signal.SIGTERM)
                click.echo(f"Sent SIGTERM to leftover Postgres PID {pid}.")
            except ProcessLookupError:
                pass

    # 4) Remove stale lock file
    if os.path.isfile(pid_file):
        try:
            os.remove(pid_file)
            click.echo("Removed stale postmaster.pid")
        except OSError as e:
            click.echo(f"Failed to remove postmaster.pid: {e}", err=True)

    click.echo("PostgreSQL fully stopped.")


@cli.command(name="clear-database")
def cli_clear_database():
    """Drop all tables from the Finance database."""
    if click.confirm("Are you sure you want to clear the database?", default=False):
        clear_database()
        click.echo("Database cleared.")
    else:
        click.echo("Aborting database clear.")


@cli.command(name="start-app")
@click.pass_context
def cli_start_app(ctx):
    ctx.invoke(cli_stop_postgres)
    ctx.invoke(cli_start_postgres)
    app_dir = os.path.join(os.path.dirname(__file__), "app")

    # Start React in background
    react_proc = subprocess.Popen([npm_command, "run", "dev"], cwd=app_dir)

    # Start API using uvicorn.run() instead of subprocess
    try:
        import uvicorn

        uvicorn.run(
            "src.api.main:app", host="0.0.0.0", port=8000, reload=True, log_level="info"
        )
    finally:
        react_proc.terminate()
        react_proc.wait(timeout=5)


@cli.command(name="debug-app")
@click.pass_context
def cli_debug_app(ctx):
    # Restart Postgres as you already have
    ctx.invoke(cli_stop_postgres)
    ctx.invoke(cli_start_postgres)

    # Start React in background
    app_dir = os.path.join(os.path.dirname(__file__), "app")
    react_proc = subprocess.Popen(
        [npm_command, "run", "dev"],
        cwd=app_dir,
        shell=False,
    )

    # Start API in debug mode
    try:
        import uvicorn

        uvicorn.run(
            "src.api.main:app",
            host="0.0.0.0",
            port=8000,
            reload=False,
            log_level="debug",
        )
    finally:
        react_proc.terminate()
        react_proc.wait(timeout=5)


if __name__ == "__main__":
    cli()
