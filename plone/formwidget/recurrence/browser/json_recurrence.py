from dateutil import rrule
import datetime
import json
import re

from zope.i18n import translate, interpolate

from Products.Five import BrowserView
from Products.CMFPlone.i18nl10n import (_interp_regex, datetime_formatvariables,
     name_formatvariables, monthname_msgid, monthname_msgid_abbr, weekdayname_msgid,
     weekdayname_msgid_abbr)

BATCH_DELTA = 3 # How many batches to show before + after current batch
BATCH_SIZE = 10 # How many items per batch

# Translations from dateinput formatting to Plone translation strings
# See http://flowplayer.org/tools/dateinput/index.html
DATEFORMAT_XLATE = [
    (re.compile(pattern), replacement) for (pattern, replacement) in (
        ('dddd', '${A}'),
        ('ddd', '${a}'),
        ('dd', '${d}'),
        ('!%d', '${e}'), # Will include a leading space for 1-9
        ('mmmm', '${B}'),
        ('mmm', '${b}'),
        ('mm', '${m}'),
        ('!%m', '${m}'), # Will include leading zero
        ('yyyy', '${Y}'),
        ('yy', '${y}'),
    )
]

def dateformat_xlate(dateformat):
    for regexp, replacement in DATEFORMAT_XLATE:
        dateformat = regexp.sub(replacement, dateformat)
    return dateformat

class RecurrenceView(BrowserView):

    def __call__(self):
        req = self.request
        req.response.setHeader("Content-type", "application/json")
        json_string = self.json_string
        return json.dumps(json_string)

    @property
    def json_string(self):
        occurrences = []
        data = self.request.form
        # Check for required parameters:
        for x in ('year', 'month', 'day', 'rrule', 'format'):
            assert x in data

        # Translate from the js dateformat style to the i18n style
        date_format = dateformat_xlate(data['format'])
        start_date = datetime.datetime(int(data['year']),
                                       int(data['month']),
                                       int(data['day']))
        rule = rrule.rrulestr(data['rrule'], dtstart=start_date)
        iterator = iter(rule)

        if 'batch_size' in data:
            batch_size = int(data['batch_size'])
        else:
            batch_size = BATCH_SIZE

        if 'start' in data:
            start = int(data['start'])
        else:
            start = 0

        cur_batch = start // batch_size
        start = cur_batch * batch_size # Avoid stupid start-values

        if hasattr(rule, '_exdate'):
            exdates = sorted(rule._exdate)
        else:
            exdates = []

        # Loop through the start first dates, to skip them:
        i = 0
        occurrences = []
        while True:
            try:
                # Get a date
                date = iterator.next()
            except StopIteration:
                # No more dates
                break
            while exdates and date > exdates[0]:
                # There are exdates that appear before this date:
                if i < start:
                    # Skip them
                    exdates.pop(0)
                    i += 1
                else:
                    # include them
                    exdate = exdates.pop(0)
                    occurrences.append({'date': exdate.strftime('%Y%m%dT%H%M%S'),
                                        'formattedDate': self.date_format(exdate, date_format),
                                        'type': 'exdate',})
                    i += 1

            if i >= batch_size + start:
                break # We are done!

            i += 1
            if i <= start:
                # We are still iterating up to the first event, so skip this:
                continue

            # Add it to the results
            if date in getattr(rule, '_rdate', []):
                occurrence_type = 'rdate'
            elif date == start_date:
                occurrence_type = 'start'
            else:
                occurrence_type = 'rrule'

            occurrences.append({'date': date.strftime('%Y%m%dT%H%M%S'),
                                'formattedDate': self.date_format(date, date_format),
                                'type': occurrence_type,})

        while exdates:
            # There are exdates that are after the end of the recurrence.
            # Excluding the last dates make no sense, as you can change the
            # range instead, but we need to support it anyway.
            exdate = exdates.pop(0)
            occurrences.append({'date': exdate.strftime('%Y%m%dT%H%M%S'),
                                'formattedDate': exdate.strftime(date_format),
                                'type': 'exdate',})

        # Calculate no of occurrences, but only to a max of three times
        # the batch size. This will support infinite recurrence in a
        # useable way, as there will always be more batches.
        first_batch = max(0, cur_batch - BATCH_DELTA)
        last_batch = max(BATCH_DELTA * 2, cur_batch + BATCH_DELTA)
        maxcount = (batch_size * last_batch) - start

        num_occurrences = 0
        while True:
            try:
                iterator.next()
                num_occurrences += 1
            except StopIteration:
                break
            if num_occurrences >= maxcount:
                break

        # Total number of occurrences:
        num_occurrences += batch_size + start

        max_batch = (num_occurrences - 1)//batch_size
        if last_batch > max_batch:
            last_batch = max_batch
            first_batch = max(0, max_batch - (BATCH_DELTA * 2))

        batches = [((x * batch_size) + 1, (x + 1) * batch_size) for x in range(first_batch, last_batch + 1)]
        batch_data = {'start': start,
                      'end': num_occurrences,
                      'batch_size': batch_size,
                      'batches': batches,
                      'currentBatch': cur_batch - first_batch,
                      }

        result = {'occurrences': occurrences, 'batch': batch_data}
        return result

    def date_format(self, time, formatstring):
        # This is a simplified version of Products.CMFPlone.i18nl10n.ulocalized_time
        # that can take any format string.

        # ${a}        Locale's abbreviated weekday name.
        # ${A}        Locale's full weekday name.
        # ${b}        Locale's abbreviated month name.
        # ${B}        Locale's full month name.
        # ${d}        Day of the month as a decimal number [01,31].
        # ${H}        Hour (24-hour clock) as a decimal number [00,23].
        # ${I}        Hour (12-hour clock) as a decimal number [01,12].
        # ${m}        Month as a decimal number [01,12].
        # ${M}        Minute as a decimal number [00,59].
        # ${p}        Locale's equivalent of either AM or PM.
        # ${S}        Second as a decimal number [00,61].
        # ${y}        Year without century as a decimal number [00,99].
        # ${Y}        Year with century as a decimal number.
        # ${Z}        Time zone name (no characters if no time zone exists).

        # get the format elements used in the formatstring
        mapping = {}
        formatelements = _interp_regex.findall(formatstring)
        # reformat the ${foo} to foo
        formatelements = [el[2:-1] for el in formatelements]

        # add used elements to mapping
        elements = [e for e in formatelements if e in datetime_formatvariables]

        # add weekday name, abbr. weekday name, month name, abbr month name
        week_included = True
        month_included = True

        name_elements = [e for e in formatelements if e in name_formatvariables]
        if not ('a' in name_elements or 'A' in name_elements):
            week_included = False
        if not ('b' in name_elements or 'B' in name_elements):
            month_included = False

        for key in elements:
            mapping[key]=time.strftime('%'+key)

        if week_included:
            weekday = int(time.strftime('%w')) # weekday, sunday = 0
            if 'a' in name_elements:
                mapping['a']=weekdayname_msgid_abbr(weekday)
            if 'A' in name_elements:
                mapping['A']=weekdayname_msgid(weekday)
        if month_included:
            monthday = int(time.strftime('%m')) # month, january = 1
            if 'b' in name_elements:
                mapping['b']=monthname_msgid_abbr(monthday)
            if 'B' in name_elements:
                mapping['B']=monthname_msgid(monthday)

        # translate translateable elements
        for key in name_elements:
            mapping[key] = translate(mapping[key], 'plonelocales', context=self.request, default=mapping[key])

        # Apply the data to the format string:
        return interpolate(formatstring, mapping)
