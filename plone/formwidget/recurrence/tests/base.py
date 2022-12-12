"""Base module for unittesting"""
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import unittest


class PloneFormwidgetRecurrenceLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""

        import plone.app.z3cform

        self.loadZCML(package=plone.app.z3cform)

        import plone.formwidget.recurrence

        self.loadZCML(package=plone.formwidget.recurrence)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        self.applyProfile(portal, "plone.formwidget.recurrence:default")


FIXTURE = PloneFormwidgetRecurrenceLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="PloneFormwidgetRecurrenceLayer:Integration"
)
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="PloneFormwidgetRecurrenceLayer:Functional"
)


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
