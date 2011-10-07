import zope.component
import zope.interface
import zope.schema.interfaces
from zope.site import hooks
from zope.traversing.browser import absoluteURL
from z3c.form.widget import Widget, FieldWidget
from z3c.form.browser import widget
from z3c.form.interfaces import IWidget, IFieldWidget, IFormLayer
from plone.formwidget.recurrence.browser.i18n import translations

class IRecurrenceWidget(IWidget):
    """Recurrence widget."""

class RecurrenceWidget(widget.HTMLTextAreaWidget, Widget):
    """Recurrence widget implementation."""
    zope.interface.implementsOnly(IRecurrenceWidget)

    klass = u'recurrence-widget'
    value = u''
    
    def update(self):
        super(RecurrenceWidget, self).update()
        widget.addFieldClass(self)
        
    def site_url(self):
        site = hooks.getSite()
        return absoluteURL(hooks.getSite(), self.request)

    def translation(self):
        return translations(self.request)

@zope.component.adapter(zope.schema.interfaces.IField, IFormLayer)
@zope.interface.implementer(IFieldWidget)
def RecurrenceFieldWidget(field, request):
    """IFieldWidget factory for RecurrenceWidget."""
    return FieldWidget(field, RecurrenceWidget(request))
