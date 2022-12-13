from plone.formwidget.recurrence.z3cform.interfaces import IRecurrenceField
from zope import schema
from zope.interface import implementer


@implementer(IRecurrenceField)
class RecurrenceField(schema.Text):
    pass
