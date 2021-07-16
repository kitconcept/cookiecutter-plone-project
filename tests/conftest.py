"""Pytest configuration."""

import pytest


@pytest.fixture(scope="session")
def context() -> dict:
    """Cookiecutter context."""
    return {
        "repository": "kitconcept-core",
        "project_title": "kitconcept Core",
        "project_namespace": "kitconcept",
        "project_name": "core",
    }


@pytest.fixture(scope="session")
def cutter_result(cookies_session, context):
    """Cookiecutter result."""
    return cookies_session.bake(extra_context=context)
