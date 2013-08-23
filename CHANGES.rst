Changelog
=========

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
