# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import polklibrary.content.transfer


class PolklibraryContentTransferLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=polklibrary.content.transfer)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.content.transfer:default')


POLKLIBRARY_CONTENT_TRANSFER_FIXTURE = PolklibraryContentTransferLayer()


POLKLIBRARY_CONTENT_TRANSFER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_CONTENT_TRANSFER_FIXTURE,),
    name='PolklibraryContentTransferLayer:IntegrationTesting'
)


POLKLIBRARY_CONTENT_TRANSFER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_CONTENT_TRANSFER_FIXTURE,),
    name='PolklibraryContentTransferLayer:FunctionalTesting'
)


POLKLIBRARY_CONTENT_TRANSFER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_CONTENT_TRANSFER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PolklibraryContentTransferLayer:AcceptanceTesting'
)
