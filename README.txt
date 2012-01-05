Introduction
============

The plone.formwidget.recurrence widget provides an Archetype and a z3cform
widget for recurrance.

The main GUI work is done with the jquery.recurrenceinput.js widget from
http://github.com/collective/jquery.recurrenceinput.js .

This widget also provides a simple textarea where a RFC 5545
compliant recurrence rule can be entered, if javascript is not available.

The resulting value of the widget is a RFC5445 compliant recurrence rule
string, ready to be used with python-dateutil's rrulestr.

Usage
-----

See plone/formwidget/recurrence/example .


For developers: Updating the javascript
---------------------------------------

The javascript files in plone/formwidget/recurrence/browser/lib comes from
jquery.recurrenceinput.js. There is two modifications needed:

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

If you also copy in the default css, you need to change a couple of paths in 
jquery.recurrenceinput.css:

    div.rioccurrences a.rrule {
        background-image: url(delete.png);
        color: transparent;
    }
    
    div.rioccurrences a.rdate {
        background-image: url(delete.png);
        color: transparent;
    }
    
    div.rioccurrences a.exdate {
        background-image: url(undelete.png);
        color: transparent;
    }
    
    div.rioccurrencesactions a.rirefreshbutton {
        background-image: url(refresh.png);
        color: transparent;
        margin-top: 4px;
        margin-right: 5px;
        
    }

Should be:

    div.rioccurrences a.rrule {
        background-image: url(++resource++jquery.recurrenceinput.delete.png);
        color: transparent;
    }
    
    div.rioccurrences a.rdate {
        background-image: url(++resource++jquery.recurrenceinput.delete.png);
        color: transparent;
    }
    
    div.rioccurrences a.exdate {
        background-image: url(++resource++jquery.recurrenceinput.undelete.png);
        color: transparent;
    }
    
    div.rioccurrencesactions a.rirefreshbutton {
        background-image: url(++resource++jquery.recurrenceinput.refresh.png);
        color: transparent;
        margin-top: 4px;
        margin-right: 5px;
    }

And the div.riform should have an additional font-size:

div.riform {
    padding: 1em;
    background-color: white;
    box-shadow: 0 0 3em 0.5em #666;
    line-height: 2;
    -moz-box-shadow: 0 0 3em 0.5em #666;
    -webkit-box-shadow: 0 0 3em #666;
    font-size: 80%;  // <- This one is Plone specific.
}

That is all the changes necessary, unless there are changes to the labels, in which
case you need to update plone/formwidget/recurrance/browser/i18n.py and the translations
to support the new labels.


Contributors
------------

This package is originally created by Tom Gross (tomgross).
Other contributors include Johannes Raggam (thet) and Lennart Regebro (regebro).
