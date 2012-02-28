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
want the Archetypes or the z3c.form widget, or both. For example:

    [buildout]
    eggs += plone.formwidget.recurrence[archetypes]
    
or 

    [buildout]
    eggs += plone.formwidget.recurrence[z3cform]
    
or

    install_requires=[
       'plone.formwidget.recurrence[z3cform,archetypes]',
    ]

Usage
-----

See plone/formwidget/recurrence/example .


For developers: Updating the javascript
---------------------------------------

The javascript files in plone/formwidget/recurrence/browser/lib comes from
jquery.recurrenceinput.js. There is one modification needed:

In jquery.recurrenceinput.js there are two submit buttons near the end
of the FORMTMPL definition:

                '<div class="ributtons">',
                    '<input',
                        'type="submit"',
                        'class="ricancelbutton"',
                        'value="${i18n.cancel}" />',
                    '<input',
                        'type="submit"',
                        'class="risavebutton"',
                        'value="${i18n.save}" />',
                '</div>',

When the javascript files are updated from jquery.recurrenceinput.form.js, 
these buttons need to have the "allowMultiSubmit" class, to prevent Plone's
warnings against clicking the same submit button multiple times. Add those
to the buttons class, so it looks like this:

                '<div class="ributtons">',
                    '<input',
                        'type="submit"',
                        'class="ricancelbutton allowMultiSubmit"',
                        'value="${i18n.cancel}" />',
                    '<input',
                        'type="submit"',
                        'class="risavebutton allowMultiSubmit"',
                        'value="${i18n.save}" />',
                '</div>',


That is all the changes necessary, unless there are changes to the labels, in which
case you need to update plone/formwidget/recurrence/browser/i18n.py and the translations
to support the new labels.


Contributors
------------

This package is originally created by Tom Gross (tomgross).
Other contributors include Johannes Raggam (thet) and Lennart Regebro (regebro).
