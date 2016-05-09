Changelog
=========

2.1.0 (2016-05-09)
------------------

New:

- Use plone i18n domain.  [klinger]

Fixes:

- Restructure tests: Move example type into own submodule.
  [thet]


2.0.2 (2015-12-03)
------------------

Fixes:

- Removed unittest2 dependency.
  [gforcada]
- Fix list index out of range at pagination.
  [julianhandl]


2.0.1 (2015-06-05)
------------------

- Fix translations.
  [thet]


2.0 (2015-03-04)
----------------

- Make widget work with Plone 5 recurrence pattern
  [vangheem]


1.2.5 (2014-07-22)
------------------

- Fix error on ie9 when rendering the recurrence widget inside an overlay.
  [deiferni]


1.2.4 (2014-07-17)
------------------

- Backport from jquery.recurrenceinput.js:
  Fix a condition, where the ``startdate`` string literal was checked, if it's
  an instance of ``String``, which returned False. This led to the case, where
  the list of occurrences wasn't shown. String literals should be checked
  with``typeof`` instead of ``instanceof``.
  See: http://stackoverflow.com/a/203757/3036508
  [thet]


1.2.3 (2014-05-06)
------------------

- Integrate latest changes from plone.formwidget.recurrence, which fixes an
  issue introduced with last version, where the recurrence overlay couldn't be
  opened with plone.formwidget.datetime based start fields on Dexterity
  objects.
  [thet]


1.2.2 (2014-04-24)
------------------

- plone.app.widgets support: Let the z3c.form widget's get_start_field method
  prefer 'name' attribute over the 'id' attribute. Looks like, with
  plone.app.widgets the rendered input field doesn't have an 'id' attribute any
  more. Also, integrate lates changes from jquery.recurrenceinput.js, which
  also handles 'name' attributes when trying to get the start field from the
  surrounding form.
  [thet]

- Register plone.app.jquerytools dateinput JavaScript for the 'default' bundle.
  plone.app.widgets registers it for 'deprecated', but we need it here and it
  can peacefully coexist with the new pickadate.
  [thet]


1.2.1 (2014-03-27)
------------------

- Change boolean expressions to conditional expressions, which to avoid wrong
  evaluation if the "and" path test evaluates to False. Really fixes #10.
  [thet]


1.2 (2014-02-12)
----------------

- Fix Problem in AT based widget with a wrong first_day offset, where it didn't
  display weekdays properly. Fixes #10.
  [thet]

- Replace test dependency on plone.formwidget.datetime with plone.app.z3cform.
  [amleczko]

- Added basque translation.
  [erral]

- Add some missing german translations.
  [msom]

- Depend on own extra requirements in test extra in setup.py.
  [thet]


1.1 (2013-11-14)
----------------

- plone.app.widgets compatibility.
  [garbas]

- Add Dutch translation.
  [khink]

- Show [1-N] in current batch instead of always [1-10]
  https://github.com/plone/plone.app.event/issues/77
  [khink]


1.0 (2013-11-06)
----------------

- Update jquery.recurrenceinput.js:
  [thet]

  - Fire change events when rrule value is updated. [deiferni]
  - Default to one week of daily occurrences, instead of 10. Fixes #5. [gyst]
  - Fix ie8 startdate and fire events when changing checkbox values [deiferni]
  - Make "repeat forever" button optional [deiferni]
  - When there is no recurrence rule, the edit button should show "Add...", not
    "Edit..." [thet]
  - Remove ambiguous recurrence rule checkbox, which lead to UX confusion due
    to double negation (unchecked checkbox said "no recurrence rule") and add
    instead a "Delete" button. [thet]

- Add a widget parameter to optionally disable the repeat forever option
  [deiferni]


1.0b11 (2013-08-23)
-------------------

- Return a 400 Bad Request to bots calling @@json_recurrence. Fixes #4.
  [href]


1.0b10 (2013-07-21)
-------------------

- Fix javascript error in IE7/IE8 on Windows XP -> "Unable to modify the parent
  container element before the child element is closed"
  [href]

- Remove the ParameterizedWidgetFactory in favor of form schema hints for
  widget parameters which is available since plone.autoform 1.4.
  [thet]

- For the z3cform widget, remove widget adaptee registration from ZCML code and
  keep it in Python code. More appropriate z3c.form class hierarchy for the
  widget. Cleanup.
  [thet]

- Provide a RecurrenceField schema field which can be used instead of
  zope.schema.Text. This ensures that the recurrence widget is used even
  without form schema hints in bare z3c.form forms.
  [thet]


1.0b9 (2013-05-27)
------------------

- Remove one unnecessary div around AT's edit macro.
  [thet]

- Register CSS and JS resources in it's registries instead of including them in
  the template. Add a GS profile for that.
  [thet]

- Fix "TypeError: 'use strict' is not a function". Fixes #3.
  [pbauer]


1.0b8 (2013-02-14)
------------------

- Fix widget showing 'undefined' for saturdays.
  [href]


1.0b7 (2013-02-08)
------------------

- Let occurrences preview show the correct daynames and not by one day off.
  Fixes https://github.com/plone/plone.app.event/issues/69
  [thet]

- Configure ributtonExtraClass with 'allowMultiSubmit'. This prevent Plone's
  warnings against clicking the same submit button multiple times. There is no
  need to customize the FORMTMPL anymore when updating the javascript from
  jquery.recurrenceinput.js.
  [thet]

- Make first_day parameter also configurable for AT and z3cform widgets.
  [thet]

- Move test related sample types to test directory and clean up package.
  [thet]


1.0b6 (2012-10-31)
------------------

- Fix ajax call to get recurrence occurrences and corresponding error message.
  [thet]


1.0b5 (2012-10-29)
------------------

- Include new release of jquery.recurrenceinput.js 1.0rc1.
  [thet]


1.0b4 (2012-10-12)
------------------

- jQueryTools DateInput localization fixed.
  [vsomogyi]

- Updated to latest jquery.recurrenceinput.js
  (8db74cee2bd53794726591c5ac8c8b3814778cbc) to fix a problem with IE8 and
  older.
  [dokai]

- Added Finnish translation.
  [dokai]


1.0b3 (2012-03-12)
------------------

- By default, preselect the BYOCCURRENCES "End recurrence" field, so that
  recurrence rules with unlimited occurences are not selected by accident but
  intentionally (from jquery.recurrenceinput.js).
  [thet]

- Include z3c.form's meta.zcml, so widgetsTemplate directive is registered.
  [thet]

- For conditional zcml incudes, use zcml:condition instead of zcml:provides.
  [thet]


1.0b2 (2012-02-28)
------------------

- Reorganization to make it possible to install only the Archetypes or
  the z3c.form widget. [regebro]


1.0b1 (2012-02-01)
------------------

- Initial release
