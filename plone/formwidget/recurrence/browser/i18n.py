from plone.formwidget.recurrence import _
from plone.formwidget.recurrence import pl_message
from zope.i18n import translate


def translations(request):
    translation_table = dict(
        displayUnactivate=translate(_("display_unactivate"), context=request),
        displayActivate=translate(_("display_activate"), context=request),
        add_rules=translate(_("add_rules"), context=request),
        edit_rules=translate(_("edit_rules"), context=request),
        delete_rules=translate(_("delete_rules"), context=request),
        add=translate(_("add"), context=request),
        refresh=translate(_("refresh"), context=request),
        title=translate(_("title"), context=request),
        preview=translate(_("preview"), context=request),
        addDate=translate(_("add_date"), context=request),
        recurrenceType=translate(_("recurrence_type"), context=request),
        dailyInterval1=translate(_("daily_interval_1"), context=request),
        dailyInterval2=translate(_("daily_interval_2"), context=request),
        weeklyInterval1=translate(_("weekly_interval_1"), context=request),
        weeklyInterval2=translate(_("weekly_interval_2"), context=request),
        weeklyWeekdays=translate(_("weekly_weekdays"), context=request),
        weeklyWeekdaysHuman=translate(_("weekly_weekdays_human"), context=request),
        monthlyInterval1=translate(_("monthly_interval_1"), context=request),
        monthlyInterval2=translate(_("monthly_interval_2"), context=request),
        monthlyDayOfMonth1=translate(_("monthly_day_of_month_1"), context=request),
        monthlyDayOfMonth1Human=translate(
            _("monthly_day_of_month_1_human"), context=request
        ),
        monthlyDayOfMonth2=translate(_("monthly_day_of_month_2"), context=request),
        monthlyDayOfMonth3=translate(_("monthly_day_of_month_3"), context=request),
        monthlyDayOfMonth4=translate(_("monthly_day_of_month_4"), context=request),
        monthlyWeekdayOfMonth1=translate(
            _("monthly_weekday_of_month_1"), context=request
        ),
        monthlyWeekdayOfMonth1Human=translate(
            _("monthly_weekday_of_month_1_human"), context=request
        ),
        monthlyWeekdayOfMonth2=translate(
            _("monthly_weekday_of_month_2"), context=request
        ),
        monthlyWeekdayOfMonth3=translate(
            _("monthly_weekday_of_month_3"), context=request
        ),
        monthlyRepeatOn=translate(_("monthly_repeat_on"), context=request),
        yearlyInterval1=translate(_("yearly_interval_1"), context=request),
        yearlyInterval2=translate(_("yearly_interval_2"), context=request),
        yearlyDayOfMonth1=translate(_("yearly_day_of_month_1"), context=request),
        yearlyDayOfMonth1Human=translate(
            _("yearly_day_of_month_1_human"), context=request
        ),
        yearlyDayOfMonth2=translate(_("yearly_day_of_month_2"), context=request),
        yearlyDayOfMonth3=translate(_("yearly_day_of_month_3"), context=request),
        yearlyWeekdayOfMonth1=translate(
            _("yearly_weekday_of_month_1"), context=request
        ),
        yearlyWeekdayOfMonth1Human=translate(
            _("yearly_weekday_of_month_1_human"), context=request
        ),
        yearlyWeekdayOfMonth2=translate(
            _("yearly_weekday_of_month_2"), context=request
        ),
        yearlyWeekdayOfMonth3=translate(
            _("yearly_weekday_of_month_3"), context=request
        ),
        yearlyWeekdayOfMonth4=translate(
            _("yearly_weekday_of_month_4"), context=request
        ),
        yearlyRepeatOn=translate(_("yearly_repeat_on"), context=request),
        range=translate(_("range"), context=request),
        rangeNoEnd=translate(_("range_no_end"), context=request),
        rangeByOccurrences1=translate(_("range_by_occurrences_1"), context=request),
        rangeByOccurrences1Human=translate(
            _("range_by_occurrences_1_human"), context=request
        ),
        rangeByOccurrences2=translate(_("range_by_occurrences_2"), context=request),
        rangeByEndDate=translate(_("range_by_end_date"), context=request),
        rangeByEndDateHuman=translate(_("range_by_end_date_human"), context=request),
        including=translate(_("including"), context=request),
        cancel=translate(_("cancel"), context=request),
        save=translate(_("save"), context=request),
        recurrenceStart=translate(_("recurrence_start"), context=request),
        additionalDate=translate(_("additional_date"), context=request),
        include=translate(_("include"), context=request),
        exclude=translate(_("exclude"), context=request),
        remove=translate(_("remove"), context=request),
        orderIndexes=[
            translate(_("order_indexes_first"), context=request),
            translate(_("order_indexes_second"), context=request),
            translate(_("order_indexes_third"), context=request),
            translate(_("order_indexes_fourth"), context=request),
            translate(_("order_indexes_last"), context=request),
        ],
        months=[
            translate(pl_message("month_jan"), context=request),
            translate(pl_message("month_feb"), context=request),
            translate(pl_message("month_mar"), context=request),
            translate(pl_message("month_apr"), context=request),
            translate(pl_message("month_may"), context=request),
            translate(pl_message("month_jun"), context=request),
            translate(pl_message("month_jul"), context=request),
            translate(pl_message("month_aug"), context=request),
            translate(pl_message("month_sep"), context=request),
            translate(pl_message("month_oct"), context=request),
            translate(pl_message("month_nov"), context=request),
            translate(pl_message("month_dec"), context=request),
        ],
        shortMonths=[
            translate(pl_message("month_jan_abbr"), context=request),
            translate(pl_message("month_feb_abbr"), context=request),
            translate(pl_message("month_mar_abbr"), context=request),
            translate(pl_message("month_apr_abbr"), context=request),
            translate(pl_message("month_may_abbr"), context=request),
            translate(pl_message("month_jun_abbr"), context=request),
            translate(pl_message("month_jul_abbr"), context=request),
            translate(pl_message("month_aug_abbr"), context=request),
            translate(pl_message("month_sep_abbr"), context=request),
            translate(pl_message("month_oct_abbr"), context=request),
            translate(pl_message("month_nov_abbr"), context=request),
            translate(pl_message("month_dec_abbr"), context=request),
        ],
        weekdays=[
            translate(pl_message("weekday_sun"), context=request),
            translate(pl_message("weekday_mon"), context=request),
            translate(pl_message("weekday_tue"), context=request),
            translate(pl_message("weekday_wed"), context=request),
            translate(pl_message("weekday_thu"), context=request),
            translate(pl_message("weekday_fri"), context=request),
            translate(pl_message("weekday_sat"), context=request),
        ],
        shortWeekdays=[
            translate(pl_message("weekday_sun_abbr"), context=request),
            translate(pl_message("weekday_mon_abbr"), context=request),
            translate(pl_message("weekday_tue_abbr"), context=request),
            translate(pl_message("weekday_wed_abbr"), context=request),
            translate(pl_message("weekday_thu_abbr"), context=request),
            translate(pl_message("weekday_fri_abbr"), context=request),
            translate(pl_message("weekday_sat_abbr"), context=request),
        ],
        longDateFormat=translate(_("long_date_format"), context=request),
        shortDateFormat=translate(
            pl_message("date_format_short_datepicker"), context=request
        ),
        unsupportedFeatures=translate(_("unsupported_features"), context=request),
        noTemplateMatch=translate(_("no_template_match"), context=request),
        multipleDayOfMonth=translate(_("multiple_day_of_month"), context=request),
        bysetpos=translate(_("bysetpos"), context=request),
        noRule=translate(_("no_rule"), context=request),
        noRepeatEvery=translate(_("no_repeat_every"), context=request),
        noEndDate=translate(_("no_end_date"), context=request),
        noRepeatOn=translate(_("no_repeat_on"), context=request),
        pastEndDate=translate(_("past_end_date"), context=request),
        noEndAfterNOccurrences=translate(
            _("no_end_after_n_occurrences"), context=request
        ),
        alreadyAdded=translate(_("already_added"), context=request),
        rtemplate=dict(
            daily=translate(_("template_daily"), context=request),
            mondayfriday=translate(_("template_mondayfriday"), context=request),
            weekdays=translate(_("template_weekdays"), context=request),
            weekly=translate(_("template_weekly"), context=request),
            monthly=translate(_("template_monthly"), context=request),
            yearly=translate(_("template_yearly"), context=request),
        ),
        # a bit wonky here, except is a reserved word
        **{"except": translate(_("except"), context=request)}
    )
    return translation_table
