from plone.formwidget.recurrence.browser.i18n import translations
from plone.formwidget.recurrence.z3cform.interfaces import IRecurrenceField
from plone.formwidget.recurrence.z3cform.interfaces import IRecurrenceWidget
from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementsOnly, implementer
from zope.site import hooks
from zope.traversing.browser import absoluteURL


class RecurrenceWidget(TextAreaWidget):
    """Recurrence widget implementation."""
    implementsOnly(IRecurrenceWidget)

    klass = u'recurrence-widget'
    value = u''
    start_field = None

    def site_url(self):
        return absoluteURL(hooks.getSite(), self.request)

    def translation(self):
        return translations(self.request)

    def read_only(self):
        return self.mode == 'display' and 'true' or 'false'

    def get_start_field(self):
        if self.mode == 'display':
            return self.id + '-start'
        return self.form.widgets[self.start_field].js_field

    def get_start_date(self):
        start = self.form.fields[self.start_field].field.get(self.context)
        return start.strftime('%Y-%m-%d %H:%M')

    def first_day(self):
        """ First day of the Week. 0..Sunday, 6..Saturday.
        You can overwrite this default value via widget configuration.
        """
        calendar = self.request.locale.dates.calendars[u'gregorian']
        return calendar.week.get('firstDay', 0)


@implementer(IFieldWidget)
@adapter(IRecurrenceField, IFormLayer)
def RecurrenceFieldWidget(field, request):
    """IFieldWidget factory for RecurrenceWidget."""
    return FieldWidget(field, RecurrenceWidget(request))
