from Products.Archetypes.tests.utils import makeContent
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.formwidget.recurrence.tests.base import IntegrationTestCase

TESTVALUE = "FREQ=MONTHLY;BYDAY=+3TU;COUNT=5"


class ATWidgetTestCase(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.obj = makeContent(
                self.folder, portal_type='RecurrenceType', id='testobj')
        self.field = self.obj.getField('rec')
        self.widget = self.field.widget

    def test_widget_properties(self):
        widget = self.widget
        self.assertEqual(widget.helper_js,
                ('++resource++jquery.tmpl.js',
                 '++resource++plone.formwidget.recurrence/jquery.recurrenceinput.js',))
        self.assertEqual(widget.helper_css,
                ('++resource++plone.formwidget.recurrence/integration.css',))
        self.assertEqual(widget.macro_edit, 'recurrence_widget')

        self.assertTrue(widget.startField == 'test_start_field')
        self.assertTrue(widget.startYear == 'test_start_year')
        self.assertTrue(widget.startMonth == 'test_start_month')
        self.assertTrue(widget.startDay == 'test_start_day')
        self.assertTrue(widget.first_day == 4)

    def test_widget_process(self):
        self.assertFalse(self.widget.process_form(self.obj, self.field, {}))
        self.assertEqual(
               self.widget.process_form(
                   self.obj, self.field, {'rec': TESTVALUE}),
               (TESTVALUE, {})
        )

    # TODO: A test that renders the widget
