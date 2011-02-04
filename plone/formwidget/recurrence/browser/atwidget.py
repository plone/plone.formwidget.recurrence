from pkg_resources import resource_string

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class RecurrenceWidget(BrowserView):
    """ """
    template = ViewPageTemplateFile('recurrence_widget.pt')

    @property
    def macros(self):
        return self.template.macros


class Templates(BrowserView):

    def __call__(self):
        return resource_string('plone.formwidget.recurrence.browser',
                'lib/templates.html')
