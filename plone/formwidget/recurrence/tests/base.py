from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

# setup test content types
from Products.GenericSetup import EXTENSION, profile_registry

import plone.formwidget.recurrence

ptc.setupPloneSite()

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            profile_registry.registerProfile('sample_types',
                'Recurrence Sample Content Types',
                'Extension profile including Archetypes sample content types',
                'profiles/sample_types',
                'plone.formwidget.recurrence',
                EXTENSION)
            fiveconfigure.debug_mode = True
            ptc.installPackage('plone.formwidget.recurrence', quiet=0)
            zcml.load_config('configure.zcml',
                             plone.formwidget.recurrence)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass
