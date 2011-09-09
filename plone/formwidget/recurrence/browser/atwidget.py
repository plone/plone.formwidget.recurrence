from pkg_resources import resource_string

from zope.i18n import translate

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.formwidget.recurrence import pfr_message, pl_message

PARAMETERS = u"""
{{i18n: {{display_label_unactivate: '{display_label_unactivate}',
display_label_activate: '{display_label_activate}',
reccurrence_type: '{reccurrence_type}',
daily_interval_1: '{daily_interval_1}',
daily_interval_2: '{daily_interval_2}',
weekly_interval_1: '{weekly_interval_1}',
weekly_interval_2: '{weekly_interval_2}',
weekly_weekdays: '{weekly_weekdays}',
monthly_day_of_month_1: '{monthly_day_of_month_1}',
monthly_day_of_month_2: '{monthly_day_of_month_2}',
monthly_day_of_month_3: '{monthly_day_of_month_3}',
monthly_day_of_month_4: '{monthly_day_of_month_4}',
monthly_weekday_of_month_1: '{monthly_weekday_of_month_1}',
monthly_weekday_of_month_2: '{monthly_weekday_of_month_2}',
monthly_weekday_of_month_3: '{monthly_weekday_of_month_3}',
monthly_weekday_of_month_4: '{monthly_weekday_of_month_4}',
yearly_day_of_month_1: '{yearly_day_of_month_1}',
yearly_day_of_month_2: '{yearly_day_of_month_2}',
yearly_day_of_month_3: '{yearly_day_of_month_3}',
yearly_weekday_of_month_1: '{yearly_weekday_of_month_1}',
yearly_weekday_of_month_2: '{yearly_weekday_of_month_2}',
yearly_weekday_of_month_3: '{yearly_weekday_of_month_3}',
yearly_weekday_of_month_4: '{yearly_weekday_of_month_4}',
range_label: '{range_label}',
range_no_end_label: '{range_no_end_label}',
range_by_occurences_label_1: '{range_by_occurences_label_1}',
range_by_occurences_label_2: '{range_by_occurences_label_2}',
range_by_end_date_label: '{range_by_end_date_label}',
cancel_button_label: '{cancel_button_label}',
save_button_label: '{save_button_label}',
order_indexes: [
    '{order_indexes_first}', '{order_indexes_second}', '{order_indexes_third}',
    '{order_indexes_fourth}', '{order_indexes_last}'],
months: [
    '{month_january}', '{month_february}', '{month_march}', '{month_april}',
    '{month_may}', '{month_june}', '{month_july}', '{month_august}',
    '{month_september}', '{month_october}', '{month_november}', '{month_december}'],
weekdays: [
    '{day_monday}', '{day_tuesday}', '{day_wednesday}', '{day_thirsday}',
    '{day_friday}', '{day_saturday}', '{day_sunday}'],
long_date_format: '{long_date_format}',
short_date_format: '{short_date_format}',
no_template_match: '{no_template_match}'
}} }}"""

class RecurrenceWidget(BrowserView):
    """ """
    template = ViewPageTemplateFile('recurrence_widget.pt')

    @property
    def macros(self):
        return self.template.macros
    
    def render_parameters(self):
        t = lambda x: self.context.translate(pfr_message(x))
        
        return PARAMETERS.format(
            display_label_unactivate= t(u'display_label_unactivate'),
            display_label_activate= t(u'display_label_activate'),
            reccurrence_type = t(u'reccurrence_type'),
            daily_interval_1 = t(u'daily_interval_1'),
            daily_interval_2 = t(u'daily_interval_2'),
            weekly_interval_1 = t(u'weekly_interval_1'),
            weekly_interval_2 = t(u'weekly_interval_2'),
            weekly_weekdays = t(u'weekly_weekdays'),
            monthly_day_of_month_1 = t(u'monthly_day_of_month_1'),
            monthly_day_of_month_2 = t(u'monthly_day_of_month_2'),
            monthly_day_of_month_3 = t(u'monthly_day_of_month_3'),
            monthly_day_of_month_4 = t(u'monthly_day_of_month_4'),
            monthly_weekday_of_month_1 = t(u'monthly_weekday_of_month_1'),
            monthly_weekday_of_month_2 = t(u'monthly_weekday_of_month_2'),
            monthly_weekday_of_month_3 = t(u'monthly_weekday_of_month_3'),
            monthly_weekday_of_month_4 = t(u'monthly_weekday_of_month_4'),
            yearly_day_of_month_1 = t(u'yearly_day_of_month_1'),
            yearly_day_of_month_2 = t(u'yearly_day_of_month_2'),
            yearly_day_of_month_3 = t(u'yearly_day_of_month_3'),
            yearly_weekday_of_month_1 = t(u'yearly_weekday_of_month_1'),
            yearly_weekday_of_month_2 = t(u'yearly_weekday_of_month_2'),
            yearly_weekday_of_month_3 = t(u'yearly_weekday_of_month_3'),
            yearly_weekday_of_month_4 = t(u'yearly_weekday_of_month_4'),
            range_label = t(u'range_label'),
            range_no_end_label = t(u'range_no_end_label'),
            range_by_occurences_label_1 = t(u'range_by_occurences_label_1'),
            range_by_occurences_label_2 = t(u'range_by_occurences_label_2'),
            range_by_end_date_label = t(u'range_by_end_date_label'),
            cancel_button_label = t(u'cancel_button_label'),
            save_button_label = t(u'save_button_label'),
            order_indexes_first = t(u'order_indexes_first'),
            order_indexes_second = t(u'order_indexes_second'),
            order_indexes_third = t(u'order_indexes_third'),
            order_indexes_fourth = t(u'order_indexes_fourth'),
            order_indexes_last = t(u'order_indexes_last'),
            month_january = self.context.translate(pl_message(u'month_jan')),
            month_february = self.context.translate(pl_message(u'month_feb')),
            month_march = self.context.translate(pl_message(u'month_mar')),
            month_april = self.context.translate(pl_message(u'month_apr')),
            month_may = self.context.translate(pl_message(u'month_may')),
            month_june = self.context.translate(pl_message(u'month_jun')),
            month_july = self.context.translate(pl_message(u'month_jul')),
            month_august = self.context.translate(pl_message(u'month_aug')),
            month_september = self.context.translate(pl_message(u'month_sep')),
            month_october = self.context.translate(pl_message(u'month_oct')),
            month_november = self.context.translate(pl_message(u'month_nov')),
            month_december = self.context.translate(pl_message(u'month_dec')),
            day_monday = self.context.translate(pl_message('weekday_mon')),
            day_tuesday = self.context.translate(pl_message('weekday_tue')),
            day_wednesday = self.context.translate(pl_message('weekday_wed')),
            day_thirsday = self.context.translate(pl_message('weekday_thu')),
            day_friday = self.context.translate(pl_message('weekday_fri')),
            day_saturday = self.context.translate(pl_message('weekday_sat')),
            day_sunday = self.context.translate(pl_message('weekday_sun')),
            long_date_format = self.context.translate(pl_message(u'date_format_long')),
            short_date_format = self.context.translate(pl_message(u'date_format_short')),
            no_template_match = t(u'no_template_match'),
        )


class Templates(BrowserView):

    def __call__(self):
        return resource_string('plone.formwidget.recurrence.browser',
                'lib/templates.html')
