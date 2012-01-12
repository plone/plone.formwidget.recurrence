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
    start_field = None
    
    def update(self):
        super(RecurrenceWidget, self).update()
        widget.addFieldClass(self)
        
    def site_url(self):
        site = hooks.getSite()
        return absoluteURL(hooks.getSite(), self.request)

    def translation(self):
        return translations(self.request)
    
    def read_only(self):
        return self.mode == 'display' and 'true' or 'false'
    
    def get_start_field(self):
        if self.mode == 'display':
            return self.id + '-start'
        import pdb;pdb.set_trace()
        return self.form.widgets[self.start_field].js_field
    
    def get_start_date(self):
        start = self.form.fields[self.start_field].field.get(self.context)
        return start.strftime('%Y-%m-%d %H:%M')

@zope.component.adapter(zope.schema.interfaces.IField, IFormLayer)
@zope.interface.implementer(IFieldWidget)
def RecurrenceFieldWidget(field, request):
    """IFieldWidget factory for RecurrenceWidget."""
    return FieldWidget(field, RecurrenceWidget(request))


class ParameterizedFieldWidget(object):
    zope.interface.implements(IFieldWidget)

    def __new__(cls, field, request):
        widget = FieldWidget(field, cls.widget(request))
        for k, v in cls.kw.items():
            setattr(widget, k, v)
        return widget

def ParameterizedWidgetFactory(widget, **kw):
    return type('%sFactory' % widget.__name__,
                (ParameterizedFieldWidget,),
                {'widget': widget, 'kw': kw})
