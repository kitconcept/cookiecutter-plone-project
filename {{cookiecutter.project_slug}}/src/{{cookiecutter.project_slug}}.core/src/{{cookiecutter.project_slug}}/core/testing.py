# -*- coding: utf-8 -*-
from plone import api
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import logout
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.testing import z2

import {{cookiecutter.project_slug}}.core


class {{cookiecutter.project_slug.capitalize()}}CoreLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package={{cookiecutter.project_slug}}.core)

    def setUpPloneSite(self, portal):
        setRoles(portal, TEST_USER_ID, ["Manager"])
        login(portal, TEST_USER_NAME)
        api.content.create(
            type="Document",
            id="front-page",
            title="Welcome",
            container=portal
        )
        logout()
        applyProfile(portal, "{{cookiecutter.project_slug}}.core:default")
        api.portal.set_registry_record("plone.default_language", u"en")


{{cookiecutter.project_slug.upper()}}_CORE_FIXTURE = {{cookiecutter.project_slug.capitalize()}}CoreLayer()


{{cookiecutter.project_slug.upper()}}_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=({{cookiecutter.project_slug.upper()}}_CORE_FIXTURE,),
    name="{{cookiecutter.project_slug.capitalize()}}CoreLayer:IntegrationTesting"
)


{{cookiecutter.project_slug.upper()}}_CORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=({{cookiecutter.project_slug.upper()}}_CORE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="{{cookiecutter.project_slug.capitalize()}}CoreLayer:FunctionalTesting"
)


{{cookiecutter.project_slug.upper()}}_CORE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        {{cookiecutter.project_slug.upper()}}_CORE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name="{{cookiecutter.project_slug.capitalize()}}CoreLayer:AcceptanceTesting"
)
