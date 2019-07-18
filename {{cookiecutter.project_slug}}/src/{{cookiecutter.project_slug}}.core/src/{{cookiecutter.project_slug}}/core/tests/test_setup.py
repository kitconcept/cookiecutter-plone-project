# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.CMFCore.utils import getToolByName
from {{cookiecutter.project_slug}}.core.testing import {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that {{cookiecutter.project_slug}}.core is properly installed."""

    layer = {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if {{cookiecutter.project_slug}}.core is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            "{{cookiecutter.project_slug}}.core"))

    # def test_plone_restapi_installed(self):
    #     self.assertTrue(
    #         self.installer.isProductInstalled(
    #             "plone.restapi"
    #         )
    #     )

    def test_browserlayer(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is registered.""" # noqa
        from {{cookiecutter.project_slug}}.core.interfaces import (
            I{{cookiecutter.project_slug.capitalize()}}CoreLayer)
        from plone.browserlayer import utils
        self.assertIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers()) # noqa


class TestUninstall(unittest.TestCase):

    layer = {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

        self.installer.uninstallProducts(["{{cookiecutter.project_slug}}.core"]) # noqa

    def test_product_uninstalled(self):
        """Test if {{cookiecutter.project_slug}}.core is cleanly uninstalled.""" # noqa
        self.assertFalse(self.installer.isProductInstalled(
            "{{cookiecutter.project_slug}}.core"))

    def test_browserlayer_removed(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is removed.""" # noqa
        from {{cookiecutter.project_slug}}.core.interfaces import I{{cookiecutter.project_slug.capitalize()}}CoreLayer # noqa
        from plone.browserlayer import utils
        self.assertNotIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers()) # noqa
