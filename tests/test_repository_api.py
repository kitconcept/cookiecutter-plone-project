"""Test Generator: /api."""
import pytest


API_FILES = [
    ".flake8",
    ".pyproject.toml",
    "buildout.cfg",
    "core.cfg",
    "dev.cfg",
    "live.cfg",
    "requirements.txt",
    "staging.cfg",
    "versions.cfg",
]


@pytest.mark.parametrize("filename", API_FILES)
def test_api_files(cutter_result, filename: str):
    """Test api files."""
    api_folder = cutter_result.project_path / "api"
    path = api_folder / filename
    assert path.is_file()
