Introduction
============

The plone.formwidget.recurrence widget provides an Archetype widget for
recurrance. The main GUI work is done with the jquery.recurrenceinput.js widget
from http://github.com/collective/jquery.recurrenceinput.js .

This widget also provides a simple textarea where a RFC 5545
compliant recurrence rule can be entered, if javascript is not available.

The resulting value of the widget is a dateutil.rrule object.

Usage
-----

See plone/formwidget/recurrence/example .


For developers: Updating the javascript
---------------------------------------

The javascript files in plone/formwidget/recurrence/browser/lib comes from
jquery.recurrenceinput.js. There is one modification needed:

In jquery.recurrenceinput.form.js there are two submit buttons near the end
of the file:

            <div class="${klass.buttons}">
                <input
                    type="submit"
                    class="${klass.cancel_button}"
                    value="${i18n.cancel_button_label}" />
                <input
                    type="submit"
                    class="${klass.save_button}"
                    value="${i18n.save_button_label}" />
            </div>

When the javascript files are updated from jquery.recurrenceinput.form.js, 
these buttons need to have the "allowMultiSubmit" class, to prevent Plone's
warnings against clicking the same submit button multiple times. Add those
to the buttons class, so it looks like this:

            <div class="${klass.buttons}">
                <input
                    type="submit"
                    class="${klass.cancel_button} allowMultiSubmit"
                    value="${i18n.cancel_button_label}" />
                <input
                    type="submit"
                    class="${klass.save_button} allowMultiSubmit"
                    value="${i18n.save_button_label}" />
            </div>

That is all the changes necessary.


Contributors
------------

This package is originally created by Tom Gross (tomgross).
Other contributors include Johannes Raggam (thet) and Lennart Regebro (regebro).
