"""Base module for unittesting"""
from Products.GenericSetup import EXTENSION
from Products.GenericSetup import profile_registry
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
import unittest2 as unittest


class PloneFormwidgetRecurrenceLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import plone.formwidget.recurrence
        self.loadZCML(package=plone.formwidget.recurrence)
        z2.installProduct(app, 'plone.formwidget.recurrence')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        profile_registry.registerProfile('sample_types',
            'Recurrence Sample Content Types',
            'Extension profile including Archetypes sample content types',
            'profiles/sample_types',
            'plone.formwidget.recurrence',
            EXTENSION)
        self.applyProfile(portal, 'plone.formwidget.recurrence:sample_types')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'plone.formwidget.recurrence')


FIXTURE = PloneFormwidgetRecurrenceLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="PloneFormwidgetRecurrenceLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="PloneFormwidgetRecurrenceLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
