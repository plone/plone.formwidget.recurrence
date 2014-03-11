from Products.Archetypes.tests.utils import makeContent
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.formwidget.recurrence.tests.base import IntegrationTestCase
from plone.testing.z2 import Browser

import transaction


TESTVALUE = "FREQ=MONTHLY;BYDAY=+3TU;COUNT=5"


class ATWidgetTestCase(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.obj = makeContent(
            self.folder, portal_type='RecurrenceType', id='testobj'
        )
        self.field = self.obj.getField('rec')
        self.widget = self.field.widget

        login(self.portal, TEST_USER_NAME)
        self.browser = Browser(self.layer['app'])
        self.browser.handleErrors = False
        transaction.commit()

    def tearDown(self):
        super(ATWidgetTestCase, self).tearDown()
        self.portal.manage_delObjects(['test-folder'])
        transaction.commit()

    def test_widget_properties(self):
        widget = self.widget
        self.assertEqual(widget.macro_edit, 'recurrence_widget')
        self.assertTrue(widget.startField == 'test_start_field')
        self.assertTrue(widget.startYear == 'test_start_year')
        self.assertTrue(widget.startMonth == 'test_start_month')
        self.assertTrue(widget.startDay == 'test_start_day')
        self.assertTrue(widget.first_day == 4)

    def test_widget_process(self):
        self.assertFalse(self.widget.process_form(self.obj, self.field, {}))
        self.assertEqual(
            self.widget.process_form(self.obj, self.field, {'rec': TESTVALUE}),
            (TESTVALUE, {})
        )

    def test_widget_rendering(self):
        self.browser.addHeader(
            'Authorization', 'Basic %s:%s' %
            (TEST_USER_NAME, TEST_USER_PASSWORD,)
        )
        self.browser.open(self.obj.absolute_url())
        self.browser.getLink('Edit').click()
        self.assertIn('Recurrence', self.browser.contents)
