from zope import schema
from zope.interface import implementer
from plone.formwidget.recurrence.z3cform.interfaces import IRecurrenceField


@implementer(IRecurrenceField)
class RecurrenceField(schema.Text):
    pass
