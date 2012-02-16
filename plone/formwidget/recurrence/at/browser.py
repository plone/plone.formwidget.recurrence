from pkg_resources import resource_string

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.formwidget.recurrence.browser.i18n import translations

class RecurrenceWidget(BrowserView):
    """ """
    template = ViewPageTemplateFile('widget.pt')

    @property
    def macros(self):
        return self.template.macros

    def translation(self):
        return translations(request=self.request)


class Templates(BrowserView):

    def __call__(self):
        return resource_string('plone.formwidget.recurrence.browser',
                'lib/templates.html')
