from zope import schema
from zope.interface import implements
from plone.formwidget.recurrence.z3cform.interfaces import IRecurrenceField


class RecurrenceField(schema.Text):
    implements(IRecurrenceField)
