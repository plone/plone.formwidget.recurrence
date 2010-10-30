from App.class_init import InitializeClass

from Products.Archetypes.atapi import LinesWidget
from Products.Archetypes.Registry import registerWidget


class RecurrenceWidget(LinesWidget):
    _properties = LinesWidget._properties.copy()
    _properties.update({
        'macro': "recurring_date",
        'helper_js': ('++resource++recurrence.js', 'widgets/js/textcount.js',),
        'helper_css': ('++resource++recurrence.css',),
        })


InitializeClass(RecurrenceWidget)
registerWidget(RecurrenceWidget,
               title='Recurring Date',
               description=('Renders a HTML form to enter all the info '
                            'for recurring dates.'),
               used_for=('plone.app.event.recurrence.RecurrenceField',))
