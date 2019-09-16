# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.CMFCore.utils import getToolByName
from {{cookiecutter.project_slug}}.{{cookiecutter.project_name}}.testing import {{cookiecutter.project_slug.upper()}}_{{cookiecutter.project_name}}_INTEGRATION_TESTING  # noqa
from plone import api

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that {{cookiecutter.project_slug}}.{{cookiecutter.project_name}} is properly installed."""

    layer = {{cookiecutter.project_slug.upper()}}_{{cookiecutter.project_name}}_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if {{cookiecutter.project_slug}}.{{cookiecutter.project_name}} is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            "{{cookiecutter.project_slug}}.{{cookiecutter.project_name}}"))

    # def test_plone_restapi_installed(self):
    #     self.assertTrue(
    #         self.installer.isProductInstalled(
    #             "plone.restapi"
    #         )
    #     )

    def test_browserlayer(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}{{cookiecutter.project_name}}Layer is registered.""" # noqa
        from {{cookiecutter.project_slug}}.{{cookiecutter.project_name}}.interfaces import (
            I{{cookiecutter.project_slug.capitalize()}}{{cookiecutter.project_name}}Layer)
        from plone.browserlayer import utils
        self.assertIn(I{{cookiecutter.project_slug.capitalize()}}{{cookiecutter.project_name}}Layer, utils.registered_layers()) # noqa


class TestUninstall(unittest.TestCase):

    layer = {{cookiecutter.project_slug.upper()}}_{{cookiecutter.project_name}}_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

        self.installer.uninstallProducts(["{{cookiecutter.project_slug}}.{{cookiecutter.project_name}}"]) # noqa

    def test_product_uninstalled(self):
        """Test if {{cookiecutter.project_slug}}.{{cookiecutter.project_name}} is cleanly uninstalled.""" # noqa
        self.assertFalse(self.installer.isProductInstalled(
            "{{cookiecutter.project_slug}}.{{cookiecutter.project_name}}"))

    def test_browserlayer_removed(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}{{cookiecutter.project_name}}Layer is removed.""" # noqa
        from {{cookiecutter.project_slug}}.{{cookiecutter.project_name}}.interfaces import I{{cookiecutter.project_slug.capitalize()}}{{cookiecutter.project_name}}Layer # noqa
        from plone.browserlayer import utils
        self.assertNotIn(I{{cookiecutter.project_slug.capitalize()}}{{cookiecutter.project_name}}Layer, utils.registered_layers()) # noqa
