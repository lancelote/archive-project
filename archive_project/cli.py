import sys

import click

from archive_project.main import main


@click.command(help="Zip current Python project")
@click.version_option()
def cli() -> None:
    sys.exit(main())


if __name__ == "__main__":
    cli()
