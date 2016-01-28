"""Base module for unittesting"""
from Products.CMFPlone.utils import getFSVersionTuple
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
import unittest


PLONE5 = getFSVersionTuple()[0] >= 5


class PloneFormwidgetRecurrenceLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import plone.formwidget.recurrence
        self.loadZCML(package=plone.formwidget.recurrence)

        import plone.formwidget.recurrence.tests.at_example  # install AT example types  # noqa
        self.loadZCML(package=plone.formwidget.recurrence.tests.at_example)
        z2.installProduct(app, 'plone.formwidget.recurrence.tests.at_example')

        z2.installProduct(app, 'Products.ATContentTypes')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        if PLONE5:
            # Install Products.ATContentTypes profile only for versions, where
            # it's available
            self.applyProfile(portal, 'Products.ATContentTypes:default')
        # install at example types
        self.applyProfile(
            portal,
            'plone.formwidget.recurrence.tests.at_example:sample_types'
        )

        self.applyProfile(portal, 'plone.formwidget.recurrence:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'plone.formwidget.recurrence.tests.at_example')  # noqa


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
