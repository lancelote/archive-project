from pathlib import Path
from shutil import make_archive

import click


def main() -> int:
    project = Path(".")
    target = Path.home() / "Desktop"
    zip_path = target / project.absolute().name

    make_archive(base_name=str(zip_path), format="zip", root_dir=project)

    click.echo(f"{zip_path}.zip was successfully created")
    return 0
