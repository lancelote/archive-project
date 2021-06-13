# archive-project

CLI tool to archive a Python project under the current working directory
ignoring things like `.idea/`, `.mypy_cache`, `.venv`, etc. and send the
result `zip` to the desktop

## Installation

`pip install -U --user archive-project`

> The package will be installed in your user home directory. See `pip`
> documentation about [user installs][1]. You need the installation directory
> to be present in `PATH` to run `archive-project` from the terminal.

## Usage

```console
$ archive-project --help
Usage: archive-project [OPTIONS]

  Zip current Python project

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

$ archive-project
/Users/user/Desktop/archive-project.zip was successfully created
```

## Requirements

- Python 3.8+
- macOS

[1]: https://pip.pypa.io/en/latest/user_guide/#user-installs
