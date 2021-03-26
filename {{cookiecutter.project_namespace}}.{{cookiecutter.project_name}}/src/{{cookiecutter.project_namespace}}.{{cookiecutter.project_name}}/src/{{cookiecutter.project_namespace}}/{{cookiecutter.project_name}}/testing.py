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

import {{cookiecutter.project_namespace}}.{{cookiecutter.project_name}}


class {{cookiecutter.project_namespace.capitalize()}}{{cookiecutter.project_name}}Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package={{cookiecutter.project_namespace}}.{{cookiecutter.project_name}})

    def setUpPloneSite(self, portal):
        setRoles(portal, TEST_USER_ID, ["Manager"])
        login(portal, TEST_USER_NAME)
        api.content.create(type="Document",id="front-page",title="Welcome",container=portal)
        logout()
        applyProfile(portal, "{{cookiecutter.project_namespace}}.{{cookiecutter.project_name}}:default")
        api.portal.set_registry_record("plone.default_language", u"en")


{{cookiecutter.project_namespace.upper()}}_{{cookiecutter.project_name}}_FIXTURE = {{cookiecutter.project_namespace.capitalize()}}{{cookiecutter.project_name}}Layer()


{{cookiecutter.project_namespace.upper()}}_{{cookiecutter.project_name}}_INTEGRATION_TESTING = IntegrationTesting(
    bases=({{cookiecutter.project_namespace.upper()}}_{{cookiecutter.project_name}}_FIXTURE,), name="{{cookiecutter.project_namespace.capitalize()}}{{cookiecutter.project_name}}Layer:IntegrationTesting"
)


{{cookiecutter.project_namespace.upper()}}_{{cookiecutter.project_name}}_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=({{cookiecutter.project_namespace.upper()}}_{{cookiecutter.project_name}}_FIXTURE, z2.ZSERVER_FIXTURE),
    name="{{cookiecutter.project_namespace.capitalize()}}{{cookiecutter.project_name}}Layer:FunctionalTesting",
)


{{cookiecutter.project_namespace.upper()}}_{{cookiecutter.project_name}}_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        {{cookiecutter.project_namespace.upper()}}_{{cookiecutter.project_name}}_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name="{{cookiecutter.project_namespace.capitalize()}}{{cookiecutter.project_name}}Layer:AcceptanceTesting"
)
