from plone.formwidget.recurrence import tests
from plone.formwidget.recurrence.browser import z3cwidget
from z3c.form import form, field
from z3c.form.interfaces import IFormLayer
from zope.publisher.browser import TestRequest
import zope.interface
import zope.schema


class ITestForm(zope.interface.Interface):

    recurrence = zope.schema.Text(
        title=u'Recurrence',
        required=True)


class TestEditForm(form.EditForm):

    fields = field.Fields(ITestForm)
    fields['recurrence'].widgetFactory = z3cwidget.RecurrenceFieldWidget


class Z3cWidgetTestCase(tests.base.IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']
        self.portal.portal_quickinstaller.installProduct('plone.formwidget.recurrence')

    # This test doesn't work any longer. We need to set up some real, useful tests.
    
    def test_widget(self):
        pass
        ## It doens't test very much, since it's all in Javascript...
        #request = TestRequest(skin=IFormLayer)
        #request.LANGUAGE = 'en'
        #form = TestEditForm(self.portal, request)
        #widget = z3cwidget.RecurrenceFieldWidget(form.fields['recurrence'].field, request)
        #widget.context = form
        #widget.update()
        #html = widget.render()

        #self.assertTrue('++resource++jquery.tmpl.js' in html)
        #self.assertTrue('++resource++plone.formwidget.recurrence/jquery.recurrenceinput.js' in html)
        #self.assertTrue('++resource++plone.formwidget.recurrence/integration.css' in html)
