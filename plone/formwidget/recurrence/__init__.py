from Products.CMFCore.utils import ContentInit
from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore.permissions import AddPortalContent
from plone.formwidget.recurrence.config import PROJECTNAME

from zope.i18nmessageid import MessageFactory

pfr_message = MessageFactory('plone.formwidget.recurrence')
pl_message = MessageFactory('plonelocales')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    from plone.formwidget.recurrence.examples import RecurrenceType
    RecurrenceType  # pyflakes
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = AddPortalContent,
        extra_constructors = constructors,
        ).initialize(context)
