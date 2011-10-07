import zope.interface
import zope.schema
from plone.formwidget.recurrence import browser, tests
from z3c.form.testing import TestRequest
from z3c.form import form

class ITestForm(zope.interface.Interface):
    id = zope.schema.TextLine(
        title=u'ID',
        readonly=True,
        required=True)

    recurrence = zope.schema.Text(
        title=u'Recurrence',
        required=True)

class TestEditForm(form.EditForm):

    fields = field.Fields(ITestForm)
    fields['recurrence'].widgetFactory = browser.z3cwidget.RecurrenceFieldWidget

TESTVALUE = "FREQ=MONTHLY;BYDAY=+3TU;COUNT=5"

class Z3cWidgetTestCase(tests.base.TestCase):

    def afterSetUp(self):
        self.portal.portal_quickinstaller.installProduct('plone.formwidget.recurrence')

    def test_widget_inputmode(self):
        request = TestRequest()
        widget = browser.z3cwidget.RecurrenceWidget(request)
        html = widget.render()
        
        self.assertTrue('++resource++jquery.tmpl.js' in html)
        self.assertTrue('++resource++jquery.recurrenceinput.js' in html)
        self.assertTrue('++resource++jquery.recurrenceinput.css' in html)

    def test_widget_with_form(self):
        import pdb;pdb.set_trace()
        testEdit = TestEditForm(object(), TestRequest())
        addTemplate(myEdit)
        myEdit.update()
        html = testing.render(myEdit, './/xmlns:input[@id="form-widgets-name"]')
        
        #self.assertFalse(self.widget.process_form(self.obj, self.field, {}))
        #self.assertEqual(
               #self.widget.process_form(
                   #self.obj, self.field, {'rec': TESTVALUE}),
               #(TESTVALUE, {})
        #)

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
