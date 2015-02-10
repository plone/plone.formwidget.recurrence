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
from plone.formwidget.recurrence.browser.i18n import translations

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

    def get_pattern_options(self):
        portal = getToolByName(getSite(), 'portal_url').getPortalObject()
        ajax_url = portal.absolute_url() + '/@@json_recurrence'
        request = portal.REQUEST

        first_day = self.first_day
        first_day = first_day() if safe_callable(first_day) else first_day

        params = dict(
            ajaxContentType='application/x-www-form-urlencoded; charset=UTF-8',
            ajaxURL=ajax_url,
            firstDay=first_day,
            hasRepeatForeverButton=self.show_repeat_forever,
            lang=request.LANGUAGE,
            ributtonExtraClass='allowMultiSubmit',
            startField=self.startField,
            startFieldDay=self.startFieldDay,
            startFieldMonth=self.startFieldMonth,
            startFieldYear=self.startFieldYear,
        )
        return json.dumps({
            "locationization": translations(request),
            "language": request.LANGUAGE,
            "configuration": params
        })


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
            rrule.rrulestr(value)   # TODO: rm dep. on rrule. check with regex
            assert('FREQ' in value) # TODO: check if freq before other
                                    # recurrence parms
        except (ValueError, TypeError, AssertionError):
            return "Validation failed: Please enter valid recurrence data."

        return True
validation.register(RecurrenceValidator('isRecurrence'))
