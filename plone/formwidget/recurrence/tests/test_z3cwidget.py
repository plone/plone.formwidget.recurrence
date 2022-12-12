from OFS.SimpleItem import SimpleItem
from plone.app.z3cform.widget import DateFieldWidget
from plone.formwidget.recurrence.tests.base import IntegrationTestCase
from plone.formwidget.recurrence.z3cform.widget import RecurrenceFieldWidget
from z3c.form import field
from z3c.form import form
from z3c.form.testing import TestRequest
from zope.schema.fieldproperty import FieldProperty

import json
import zope.interface
import zope.schema


class ITestForm(zope.interface.Interface):
    recurrence = zope.schema.Text(title="Recurrence", required=True)
    day = zope.schema.Date(title="Day", required=True)


@zope.interface.implementer(ITestForm)
class TestForm(SimpleItem):
    recurrence = FieldProperty(ITestForm["recurrence"])
    day = FieldProperty(ITestForm["day"])

    def __init__(self, recurrence, day):
        super(TestForm, self).__init__(id)
        self.recurrence = recurrence
        self.day = day


class TestAddForm(form.AddForm):
    fields = field.Fields(ITestForm)
    fields["recurrence"].widgetFactory = RecurrenceFieldWidget
    fields["day"].widgetFactory = DateFieldWidget


class Z3CWidgetTestCase(IntegrationTestCase):
    def setUp(self):
        self.portal = self.layer["portal"]
        request = TestRequest()
        request.LANGUAGE = "en"
        form = TestAddForm(self.portal, request)
        form.update()

        self.widget = RecurrenceFieldWidget(form.fields["recurrence"].field, request)

        self.widget.form = form
        self.widget.start_field = "day"
        self.widget.update()

    def test_widget_options(self):
        pat_options = json.loads(self.widget.get_pattern_options())
        self.assertEqual(
            {
                "ajaxContentType": "application/x-www-form-urlencoded; charset=UTF-8",
                "ajaxURL": "http://nohost/plone/@@json_recurrence",
                "firstDay": 7,
                "hasRepeatForeverButton": True,
                "lang": "en",
                "readOnly": False,
                "ributtonExtraClass": "allowMultiSubmit",
                "startField": "form.widgets.day",
            },
            pat_options["configuration"],
        )

    def test_widget_rendering(self):
        html = self.widget.render()
        self.assertIn("pat-recurrence", html)
