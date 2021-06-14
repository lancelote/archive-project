import os

import pytest
from click.testing import CliRunner


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def tmp_work_dir(request, tmp_path):
    os.chdir(tmp_path)
    yield tmp_path
    os.chdir(request.config.invocation_dir)
