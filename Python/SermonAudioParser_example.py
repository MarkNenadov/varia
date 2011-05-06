""" --== SermonAudioParser ==--

A simple python class for using SermonAudio.com's RSS feed.

 This code demonstrates a very simple usage of how to use
 Universal Feed Parser (https://code.google.com/p/feedparser/)
 and also gives some functionality specific to SermonAudio.com
 that might possibly be useful to someone out there.

 Note: To run this, you must have the Universal Feed Parser setup
 under your active Python install

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

import feedparser

class SermonAudioParser:
    """ A class to do some searching operations on sermonaudio.com's
    RSS Feed
    """

    SA_URL = "http://www.sermonaudio.com/rss_source.rss"
    sa_feed = 0
    entries = 0

    def __load_entries(self):
        """ parse feed and load items
	"""

        self.sa_feed = feedparser.parse(self.SA_URL )
        self.entries = self.sa_feed['items']


    def __init__(self):
        """ Constructor
	"""
        self.__load_entries()

    def find_by_title(self, title_match=''):
        """ Do a string search on title
        """ 
        results = []
        for entry in self.entries:
            if entry.has_key('title'):
                if (entry['title'].find(title_match) != -1):
                    results.append(entry)
        return results

    def find_by_summary(self, summary_match=''):
        """ Do a string search on summary
	"""

        results = []
        for entry in self.entries:
            if entry.has_key('summary'):
                if (entry['summary'].find(summary_match) != -1):
                    results.append(entry)
        return results

    def find_by_all(self, match=''):
        """ Do a string search on summary and title
	"""

        results = []
        for entry in self.entries:
            txt_concat = ''
            if entry.has_key('summary'):
                txt_concat += entry['summary']
            if entry.has_key('title'):
                txt_concat += entry['title']
            if (txt_concat.find(match) != -1):
                results.append(entry)
        return results

if __name__ == "__main__":

    # Tests / Sample

    SA_PARSER = SermonAudioParser()

    print "SermonAudioParser Demonstration\n\n"

    print "Feed Items with 'faith' anywhere in their title:"
    for x in SA_PARSER.find_by_title('faith'):
        print "* " + x['title'] + " - " + x['link']

    print " --- "

    print "Feed Items with 'faith' anywhere in their summary:"
    for x in SA_PARSER.find_by_summary('faith'):
        print "* " + x['title'] + " - " + x['link']

    print " --- "
        
    print "Feed Items with 'faith' anywhere in their title or summary:"
    for x in SA_PARSER.find_by_all('faith'):
        print "* " + x['title'] + " - " + x['link']


