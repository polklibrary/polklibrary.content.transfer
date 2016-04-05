# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.content.transfer.testing import POLKLIBRARY_CONTENT_TRANSFER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.content.transfer is properly installed."""

    layer = POLKLIBRARY_CONTENT_TRANSFER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.content.transfer is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.content.transfer'))

    def test_browserlayer(self):
        """Test that IPolklibraryContentTransferLayer is registered."""
        from polklibrary.content.transfer.interfaces import IPolklibraryContentTransferLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryContentTransferLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_CONTENT_TRANSFER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.content.transfer'])

    def test_product_uninstalled(self):
        """Test if polklibrary.content.transfer is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.content.transfer'))
