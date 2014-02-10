from OFS.SimpleItem import SimpleItem
from plone.app.z3cform.widget import DateFieldWidget
from plone.formwidget.recurrence.tests.base import IntegrationTestCase
from plone.formwidget.recurrence.z3cform.widget import RecurrenceFieldWidget
from z3c.form import form, field
from z3c.form.testing import TestRequest
from zope.schema.fieldproperty import FieldProperty

import zope.interface
import zope.schema


class ITestForm(zope.interface.Interface):
    recurrence = zope.schema.Text(title=u'Recurrence', required=True)
    day = zope.schema.Date(title=u'Day', required=True)


class TestForm(SimpleItem):
    zope.interface.implements(ITestForm)
    recurrence = FieldProperty(ITestForm['recurrence'])
    day = FieldProperty(ITestForm['day'])

    def __init__(self, recurrence, day):
        super(TestForm, self).__init__(id)
        self.recurrence = recurrence
        self.day = day


class TestAddForm(form.AddForm):
    fields = field.Fields(ITestForm)
    fields['recurrence'].widgetFactory = RecurrenceFieldWidget
    fields['day'].widgetFactory = DateFieldWidget


class Z3CWidgetTestCase(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_widget_rendering(self):
        request = TestRequest()
        request.LANGUAGE = 'en'
        form = TestAddForm(self.portal, request)
        form.update()

        widget = RecurrenceFieldWidget(form.fields['recurrence'].field,
                                       request)
        widget.form = form
        widget.start_field = 'day'
        widget.update()

        html = widget.render()
        self.assertIn('recurrence', html)
