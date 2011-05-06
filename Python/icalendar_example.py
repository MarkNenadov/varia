""" An incomplete experiment with building calendar functionality 
with the Python icalendar module

Tested with pylint (10/10 score with default config)

AUTHOR

Mark J. Nenadov (2011)
* Essex, Ontario
* Email: <marknenadov@gmail.com> 

LICENSING

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version

This program is distributed in the hope that it will be useful
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>. 


"""

import icalendar
from datetime import datetime

CALENDAR_FILE = "c:\\test_calendar.ics"

class TestEvent:
    """ Wraps an ICalendar event
    """

    data = ""

    def __init__(self, component=''):
        """ Constructor
	"""
        pass

    def set_data(self, working_data):
        """ Set Data for the event
        """
        self.data = working_data
		
    def get_ical_object(self):
        """ Get an Icalendar object for this event
	"""
        event = icalendar.Event()
        event.add('summary', self.data['summary'])
        event.add('dtstart', self.data['dtstart'])
        event.add('dtend', self.data['dtend'])
        event.add('dtstamp', self.data['dtstamp'])

        return event
	

class TestCalendar:
    """ Wraps an ICalendar Calendar
    """

    calendar = ""
    calendar_file = ""

    def __init__(self, calendar_file):
        """ Constructor
	"""
        self.calendar_file = calendar_file
        tmp_file = open(self.calendar_file, 'rb')
        self.calendar = icalendar.Calendar.from_string(tmp_file.read())
        tmp_file.close()

    def get_raw_content(self):
        """Get raw calendar content
        """
        return self.calendar

    def get_events(self):
        """Return all events
        """

        components = []
        for component in self.calendar.walk():
            if component.name == 'VEVENT':
                components.append(TestEvent(component))	
        return components

    def get_num_events(self):
        """ Get number of events we have
        """
        
        return len(self.get_events())

    def add_event(self, event, save=0):
        """ Add Event to calendar """

        self.calendar.add_component(event)

        if save:
            self.save_changes()

    def save_changes(self):
        """ Save changes out to file
	"""

        tmp_file = open(self.calendar_file, 'wb')
        tmp_file.write(self.calendar.as_string())
        tmp_file.close()


CAL = TestCalendar(CALENDAR_FILE)


EVENT_INFO = {}
EVENT_INFO['summary'] = "JUST AN EVENT"
EVENT_INFO['dtstart'] = datetime(2008, 3, 17, 8, 0, 0, tzinfo=icalendar.UTC)
EVENT_INFO['dtend'] = datetime(2008, 3, 17, 9, 0, 0, tzinfo=icalendar.UTC)
EVENT_INFO['dtstamp'] = datetime(2008, 3, 1, 1, 0, 0, tzinfo=icalendar.UTC)
EVENT = TestEvent()
EVENT.set_data(EVENT_INFO)

CAL.add_event(EVENT)

