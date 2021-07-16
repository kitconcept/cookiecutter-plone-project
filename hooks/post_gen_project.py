"""Create virtualenv and print a thank you note."""
from textwrap import dedent

import subprocess
import sys


try:
    import venv
    VIRTUALENV_AVAILABLE = True
except ImportError:
    VIRTUALENV_AVAILABLE = False


def prepare_environment():
    """Create venv and apply black and isort to codebase."""
    venv.create('api', with_pip=True)
    commands = [
        ['./bin/pip', 'install', '-r', 'requirements.txt'],
        ['./bin/pip', 'install', 'black'],
        ['./bin/pip', 'install', 'isort'],
        ['./bin/black', 'src/'],
        ['./bin/isort', 'src/'],
    ]
    for command in commands:
        proc = subprocess.Popen(
            command,
            shell=sys.platform.startswith('win'),
            cwd='api'
        )
        proc.wait()


if VIRTUALENV_AVAILABLE:
    try:
        prepare_environment()
    except subprocess.CalledProcessError:
        print('It was not possible to create the virtualenv. Maybe inside tox?')
    except FileNotFoundError:
        print(subprocess.check_output(['ls']))


msg = dedent("""
    ===============================================================================
    Package {{ cookiecutter.repository }} was generated.
    Now, code it, create a git repository, push to your Github account.
    Sorry for the convenience.
    ===============================================================================
""")

print(msg)
