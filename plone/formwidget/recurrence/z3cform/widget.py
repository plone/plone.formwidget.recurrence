from Products.CMFCore.utils import getToolByName
from plone.formwidget.recurrence.browser.i18n import translations
from plone.formwidget.recurrence.z3cform.interfaces import IRecurrenceField
from plone.formwidget.recurrence.z3cform.interfaces import IRecurrenceWidget
from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.component.hooks import getSite
from zope.interface import implementsOnly, implementer
from zope.traversing.browser import absoluteURL

import json


class RecurrenceWidget(TextAreaWidget):
    """Recurrence widget implementation."""
    implementsOnly(IRecurrenceWidget)

    klass = u'recurrence-widget'
    value = u''
    start_field = None
    show_repeat_forever = True

    def site_url(self):
        return absoluteURL(getSite(), self.request)

    def read_only(self):
        return self.mode == 'display'

    def get_start_field(self):
        if self.mode == 'display':
            return self.id + '-start'
        if hasattr(self.form.widgets[self.start_field], 'js_field'):
            return self.form.widgets[self.start_field].js_field
        if hasattr(self.form.widgets[self.start_field], 'name'):
            # plone.app.widgets passes name instead of id to input
            return self.form.widgets[self.start_field].name
        return self.form.widgets[self.start_field].id

    def get_start_date(self):
        start = self.form.fields[self.start_field].field.get(self.context)
        return start.strftime('%Y-%m-%d %H:%M')

    def first_day(self):
        """ First day of the Week. 0..Sunday, 6..Saturday.

        .. Note::
            This value is likely to be overwritten by the widget configuration.
        """
        calendar = self.request.locale.dates.calendars[u'gregorian']
        return calendar.week.get('firstDay', 0)

    def get_pattern_options(self):
        portal = getToolByName(getSite(), 'portal_url').getPortalObject()
        ajax_url = portal.absolute_url() + '/@@json_recurrence'
        conf = dict(
            ajaxContentType='application/x-www-form-urlencoded; charset=UTF-8',
            ajaxURL=ajax_url,
            firstDay=self.first_day(),
            hasRepeatForeverButton=self.show_repeat_forever,
            lang=self.request.LANGUAGE,
            readOnly=self.read_only(),
            ributtonExtraClass='allowMultiSubmit',
            startField=self.get_start_field(),
        )
        return json.dumps({
            "localization": translations(self.request),
            "language": self.request.LANGUAGE,
            "configuration": conf
        })


@implementer(IFieldWidget)
@adapter(IRecurrenceField, IFormLayer)
def RecurrenceFieldWidget(field, request):
    """IFieldWidget factory for RecurrenceWidget."""
    return FieldWidget(field, RecurrenceWidget(request))
