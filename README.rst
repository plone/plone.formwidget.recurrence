Introduction
============

The plone.formwidget.recurrence package provides an Archetype and a z3cform
widget for recurrence.

The main GUI work is done with the jquery.recurrenceinput.js widget from
http://github.com/collective/jquery.recurrenceinput.js .

This widget also provides a simple textarea where a RFC 5545
compliant recurrence rule can be entered, if javascript is not available.

The resulting value of the widget is a RFC5445 compliant recurrence rule
string, ready to be used with python-dateutil's rrulestr.


Installation
------------

You need to add plone.formwidget.recurrence to either your buildout, or
your product requirements. In this addition you should specify if you
want the Archetypes or the z3c.form widget, or both. For example::

  [buildout]
  eggs += plone.formwidget.recurrence[archetypes]

or::

  [buildout]
  eggs += plone.formwidget.recurrence[z3cform]

or::

  install_requires=[
     'plone.formwidget.recurrence[z3cform,archetypes]',
  ]


TODO
----

- Better test coverage.

? - Usage docs for AT and DX. Show z3c.form widget parameters via
  plone.autoform > 1.4
