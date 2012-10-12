Changelog
=========

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
