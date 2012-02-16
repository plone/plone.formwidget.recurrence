from dateutil import rrule
from zope.interface import implements
from App.class_init import InitializeClass

from Products.Archetypes.atapi import LinesWidget
from Products.Archetypes.Registry import registerWidget
from Products.validation.interfaces.IValidator import IValidator
from Products.validation import validation


class RecurrenceWidget(LinesWidget):
    _properties = LinesWidget._properties.copy()
    _properties.update({
        'macro_edit': "recurrence_widget",
        'helper_js': ('++resource++jquery.tmpl.js',
                      '++resource++plone.formwidget.recurrence/jquery.recurrenceinput.js'),
        'helper_css': ('++resource++plone.formwidget.recurrence/integration.css',),
        'startField': '',
        'startYear': '',
        'startMonth': '',
        'startDay': '',
        })


InitializeClass(RecurrenceWidget)
registerWidget(RecurrenceWidget,
               title='Recurring Date',
               description=('Renders a recurrence widget to enter all the info '
                            'for recurring dates.'),
               used_for=('plone.app.event.recurrence.RecurrenceField',))


class RecurrenceValidator(object):
    # TODO: tests
    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        try:
            rrule.rrulestr(value) # TODO: rm dep. on rrule. check with regex
            assert('FREQ' in value) # TODO: check if freq before other
                                    # recurrence parms
        except (ValueError, TypeError, AssertionError):
            return "Validation failed: Please enter valid recurrence data."

        return True
validation.register(RecurrenceValidator('isRecurrence'))
