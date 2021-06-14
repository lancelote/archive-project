from pathlib import Path
from zipfile import ZipFile

from archive_project.cli import cli


def unpack(archive: Path, to: Path) -> None:
    with ZipFile(archive.absolute()) as archive_zip_file:
        archive_zip_file.extractall(to.absolute())


def test_folder_is_correctly_archived(tmp_work_dir, cli_runner):
    file1 = tmp_work_dir / "sample1.py"
    file1.write_text("# test 1")
    file2 = tmp_work_dir / "sample2.py"
    file2.write_text("# test 2")

    desktop = Path.home() / "Desktop"
    archive = desktop / f"{tmp_work_dir.name}.zip"

    result = cli_runner.invoke(cli)

    unpack_dir = tmp_work_dir / "unpack_target"
    unpack(archive, to=unpack_dir)

    assert result.exit_code == 0
    assert len(list(desktop.glob(archive.name))) == 1
    assert len(list(unpack_dir.glob("sample*.py"))) == 2

    archive.unlink()
