from plone.formwidget.recurrence.tests.base import TestCase
from Products.Archetypes.tests.utils import makeContent

TESTVALUE = "a testvalue"
class ATWidgetTestCase(TestCase):

    def afterSetUp(self):
        self.obj = makeContent(
                self.folder, portal_type='RecurrenceType', id='testobj')
        self.field = self.obj.getField('rec')
        self.widget = self.field.widget

    def test_widget_properties(self):
        self.assertEqual(self.widget.helper_js,
                ('++resource++jquery.tmpl.js',
                 '++resource++jquery.recurrenceinput.config.js',
                 '++resource++jquery.recurrenceinput.js',))
        self.assertEqual(self.widget.helper_css,
                ('++resource++jquery.recurrenceinput.css',))
        self.assertEqual(self.widget.macro_edit, 'recurrence_widget')

    def test_widget_process(self):
        self.assertFalse(self.widget.process_form(self.obj, self.field, {}))
        self.assertEqual(
               self.widget.process_form(
                   self.obj, self.field, {'rec': TESTVALUE})
               (TESTVALUE, {})
        )

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
