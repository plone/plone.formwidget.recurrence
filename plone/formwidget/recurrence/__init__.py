from Products.CMFCore.utils import ContentInit
from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore.permissions import AddPortalContent
from plone.formwidget.recurrence.config import PROJECTNAME

from zope.i18nmessageid import MessageFactory

pfr_message = MessageFactory('plone.formwidget.recurrence')
pl_message = MessageFactory('plonelocales')

def initialize(context):
    # Example content type initialization
    import plone.formwidget.recurrence.examples
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME), PROJECTNAME, )

    ContentInit(
        '%s Content' % PROJECTNAME,
        content_types=content_types,
        permission=AddPortalContent,
        extra_constructors=constructors,
        fti=ftis,
        ).initialize(context)
