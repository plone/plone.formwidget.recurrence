from plone.formwidget.recurrence import _
from z3c.form.interfaces import IWidget
from zope.schema import ValidationError
from zope.schema.interfaces import IText


# Fields
class IRecurrenceField(IText):
    """Special marker for datetime fields that use our widget."""


# Widgets
class IRecurrenceWidget(IWidget):
    """Date widget marker for z3c.form."""


# Errors
class RecurrenceValidationError(ValidationError):
    __doc__ = _("The recurrence rule couldn't be parsed.")
