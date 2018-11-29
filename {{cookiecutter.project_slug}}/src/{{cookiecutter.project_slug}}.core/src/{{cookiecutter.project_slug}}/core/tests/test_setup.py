# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.CMFCore.utils import getToolByName
from {{cookiecutter.project_slug}}.core.testing import {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that {{cookiecutter.project_slug}}.core is properly installed."""

    layer = {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if {{cookiecutter.project_slug}}.core is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            '{{cookiecutter.project_slug}}.core'))

    def test_plone_app_imagecropping_installed(self):
        self.assertTrue(
            self.installer.isProductInstalled(
                'plone.app.imagecropping'
            )
        )

    def test_plone_restapi_installed(self):
        self.assertTrue(
            self.installer.isProductInstalled(
                'plone.restapi'
            )
        )

    def test_news_item_renamed_to_meldung(self):
        portal_types = getToolByName(self.portal, 'portal_types')
        news_item_fti = getattr(portal_types, 'News Item')
        self.assertEqual('Meldung', news_item_fti.title)

    def test_browserlayer(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is registered."""
        from {{cookiecutter.project_slug}}.core.interfaces import (
            I{{cookiecutter.project_slug.capitalize()}}CoreLayer)
        from plone.browserlayer import utils
        self.assertIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = {{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['{{cookiecutter.project_slug}}.core'])

    def test_product_uninstalled(self):
        """Test if {{cookiecutter.project_slug}}.core is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            '{{cookiecutter.project_slug}}.core'))

    def test_browserlayer_removed(self):
        """Test that I{{cookiecutter.project_slug.capitalize()}}CoreLayer is removed."""
        from {{cookiecutter.project_slug}}.core.interfaces import I{{cookiecutter.project_slug.capitalize()}}CoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(I{{cookiecutter.project_slug.capitalize()}}CoreLayer, utils.registered_layers())
