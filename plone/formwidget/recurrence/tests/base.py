from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

# XXX move this to PloneTestCase
# index has to be installed first and not deferred via @onsetup
def setupIndex():
    import Products.DateRecurringIndex
    ptc.installProduct('DateRecurringIndex')
setupIndex()

# setup test content types
from Products.GenericSetup import EXTENSION, profile_registry


profile_registry.registerProfile('Recurrence_sampletypes',
    'Recurrence Sample Content Types',
    'Extension profile including Archetypes sample content types',
    'profiles/sample_types',
    'plone.formwidget.recurrence',
    EXTENSION)
ptc.setupPloneSite(extension_profiles=[
    'plone.formwidget.recurrence:Recurrence_sampletypes'])


import plone.formwidget.recurrence


class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            ptc.installPackage('plone.formwidget.recurrence', quiet=0)
            zcml.load_config('configure.zcml',
                             plone.formwidget.recurrence)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass
