import unittest
from plone.formwidget.recurrence.tests.base import TestCase
from Products.Archetypes.tests.utils import makeContent

class ATWidgetTestCase(TestCase):

    def test_widget_properties(self):
        obj = makeContent(self.folder, portal_type='RecurrenceType', id='testobj')
        widget = obj.getField('rec').widget


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
