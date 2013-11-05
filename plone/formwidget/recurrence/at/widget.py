from App.class_init import InitializeClass
from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.atapi import LinesWidget
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_callable
from Products.validation import validation
from Products.validation.interfaces.IValidator import IValidator
from dateutil import rrule
from zope.component.hooks import getSite
from zope.interface import implements

import json


class RecurrenceWidget(LinesWidget):
    _properties = LinesWidget._properties.copy()
    _properties.update({
        'macro_edit': "recurrence_widget",
        'helper_js': (),
        'helper_css': (),
        'startField': '',
        'startFieldYear': '',
        'startFieldMonth': '',
        'startFieldDay': '',
        'first_day': '',
        'show_repeat_forever': True,
        })

    def get_recurrenceinput_params(self):
        portal = getToolByName(getSite(), 'portal_url').getPortalObject()
        ajax_url = portal.absolute_url() + '/@@json_recurrence'
        request = portal.REQUEST
        first_day = self.first_day
        first_day = safe_callable(first_day) and first_day() or first_day,

        params = dict(
            lang=request.LANGUAGE,
            startFieldDay=self.startFieldDay,
            startFieldMonth=self.startFieldMonth,
            startFieldYear=self.startFieldYear,
            startField=self.startField,
            firstDay=first_day,
            ajaxURL=ajax_url,
            ajaxContentType='application/x-www-form-urlencoded; charset=UTF-8',
            ributtonExtraClass='allowMultiSubmit',
            hasRepeatForeverButton=self.show_repeat_forever
        )
        return params

    def js_recurrenceinput_params(self):
        return json.dumps(self.get_recurrenceinput_params())


InitializeClass(RecurrenceWidget)
registerWidget(RecurrenceWidget,
               title='Recurring Date',
               description=('Renders a recurrence widget to enter all the '
                            'info for recurring dates.'),
               used_for=('plone.app.event.recurrence.RecurrenceField',))


class RecurrenceValidator(object):
    # TODO: tests
    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        try:
            rrule.rrulestr(value)  # TODO: rm dep. on rrule. check with regex
            assert('FREQ' in value)  # TODO: check if freq before other
                                     # recurrence parms
        except (ValueError, TypeError, AssertionError):
            return "Validation failed: Please enter valid recurrence data."

        return True
validation.register(RecurrenceValidator('isRecurrence'))
