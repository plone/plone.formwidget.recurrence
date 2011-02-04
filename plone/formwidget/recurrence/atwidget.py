from App.class_init import InitializeClass

from Products.Archetypes.atapi import LinesWidget
from Products.Archetypes.Registry import registerWidget


class RecurrenceWidget(LinesWidget):
    _properties = LinesWidget._properties.copy()
    _properties.update({
        'macro_edit': "recurrence_widget",
        'helper_js': ('++resource++jquery.tmpl.js',
                      '++resource++jquery.recurrenceinput.js'),
        'helper_css': ('++resource++jquery.recurrenceinput.css',),
        })


InitializeClass(RecurrenceWidget)
registerWidget(RecurrenceWidget,
               title='Recurring Date',
               description=('Renders a recurrence widget to enter all the info '
                            'for recurring dates.'),
               used_for=('plone.app.event.recurrence.RecurrenceField',))
