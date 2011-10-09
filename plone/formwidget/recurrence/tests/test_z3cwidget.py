import zope.interface
import zope.schema
from plone.formwidget.recurrence import tests
from plone.formwidget.recurrence.browser import z3cwidget
from z3c.form import testing
from z3c.form import form, field

class ITestForm(zope.interface.Interface):
    
    recurrence = zope.schema.Text(
        title=u'Recurrence',
        required=True)

class TestEditForm(form.EditForm):

    fields = field.Fields(ITestForm)
    fields['recurrence'].widgetFactory = z3cwidget.RecurrenceFieldWidget
    
    
class Z3cWidgetTestCase(tests.base.TestCase):

    def afterSetUp(self):
        self.portal.portal_quickinstaller.installProduct('plone.formwidget.recurrence')

    def test_widget(self):
        # It doens't test very much, since it's all in Javascript...
        request = testing.TestRequest()
        request.LANGUAGE = 'en'
        form = TestEditForm(self.portal, request)
        widget = z3cwidget.RecurrenceFieldWidget(form.fields['recurrence'].field, request)
        widget.update()
        html = widget.render()
        
        self.assertTrue('++resource++jquery.tmpl.js' in html)
        self.assertTrue('++resource++jquery.recurrenceinput.js' in html)
        self.assertTrue('++resource++jquery.recurrenceinput.css' in html)

def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
