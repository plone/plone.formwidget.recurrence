from Products.Archetypes.atapi import BaseSchema
from Products.Archetypes.atapi import LinesField
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import registerType
from Products.Archetypes.examples.SimpleType import SimpleType
from plone.formwidget.recurrence.at.widget import RecurrenceWidget


schema = BaseSchema.copy() + Schema((
    LinesField(
        'rec',
        widget=RecurrenceWidget(
            label='Recurrence',
            startField='test_start_field',
            startYear='test_start_year',
            startMonth='test_start_month',
            startDay='test_start_day',
            first_day=4,
        ),
    ),
))


class RecurrenceType(SimpleType):
    """A simple archetype"""
    schema = schema
    archetype_name = meta_type = "RecurrenceType"
    portal_type = 'RecurrenceType'


registerType(RecurrenceType, 'plone.formwidget.recurrence.tests.at_example')
