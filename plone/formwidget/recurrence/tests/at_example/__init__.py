from Products.Archetypes import atapi

packageName = __name__


def initialize(context):
    """Register content types through Archetypes with Zope and the CMF.
    """
    from Products.CMFCore.utils import ContentInit
    from Products.CMFCore.permissions import AddPortalContent
    from plone.formwidget.recurrence.tests.at_example import content  # noqa

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(packageName), packageName)

    for atype, constructor, fti in zip(content_types, constructors, ftis):
        ContentInit(
            "%s: %s" % (packageName, atype.portal_type),
            content_types=(atype,),
            permission = AddPortalContent,
            extra_constructors = (constructor,),
            fti = (fti,),
        ).initialize(context)
