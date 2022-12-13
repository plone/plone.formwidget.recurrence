Introduction
============

The plone.formwidget.recurrence package provides a z3cform widget for recurrence.

The main GUI work is done with the ``pat-recurrence`` pattern from mockup.

This widget provides a simple textarea where a RFC 5545 compliant
recurrence rule can be entered, if javascript is not available.

The resulting value of the widget is a RFC5445 compliant recurrence rule
string, ready to be used with python-dateutil's rrulestr.


Installation
------------

You need to add plone.formwidget.recurrence to either your buildout, or
your product requirements. For example::

  [buildout]
  eggs += plone.formwidget.recurrence[z3cform]

or::

  install_requires=[
     'plone.formwidget.recurrence[z3cform]',
  ]
