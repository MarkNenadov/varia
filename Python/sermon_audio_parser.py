""" --== SermonAudioParser ==--

A simple python class for using SermonAudio.com's RSS feed.

 This code demonstrates a very simple usage of how to use
 Universal Feed Parser (https://code.google.com/p/feedparser/)
 and also gives some functionality specific to SermonAudio.com
 that might possibly be useful to someone out there.

 Note: To run this, you must have the Universal Feed Parser setup.

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

    SERMON_AUDIO_URL = "http://www.sermonaudio.com/rss_source.rss"
    sermon_audio_feed = None
    feed_items = None

    def __load_feed_items(self):
        """ parse feed and load items
	    """

        self.sermon_audio_feed = feedparser.parse(self.SERMON_AUDIO_URL )
        self.feed_items = self.sermon_audio_feed['items']


    def __init__(self):
        """ Constructor
	    """
        self.__load_feed_items()

    def find_by_title(self, match_value=''):
        """ Do a string search on title
        """ 
        results = []
        for item in self.feed_items:
            if item.has_key('title'):
                if (item['title'].lower().find(match_value.lower()) != -1):
                    results.append(item)
        return results

    def find_by_summary(self, match_value=''):
        """ Do a string search on summary
	    """

        results = []
        for item in self.feed_items:
            if item.has_key('summary'):
                if (item['summary'].lower().find(match_value.lower()) != -1):
                    results.append(item)
        return results

    def find_by_all(self, match_value=''):
        """ Do a string search on summary and title
	    """

        return list(set(self.find_by_title(match_value) + self.find_by_summary(match_value)))

if __name__ == "__main__":

    # Tests / Sample

    SA_PARSER = SermonAudioParser()

    print "SermonAudioParser Demonstration\n\n"

    print "Feed Items with 'reformed' anywhere in their title:"
    for x in SA_PARSER.find_by_title('reformed'):
        print "* " + x['title'] + " - " + x['link']

    print " --- "

    print "Feed Items with 'reformed' anywhere in their summary:"
    for x in SA_PARSER.find_by_summary('reformed'):
        print "* " + x['title'] + " - " + x['link']

    print " --- "
        
    print "Feed Items with 'reformed' anywhere in their title or summary:"
    for x in SA_PARSER.find_by_all('reformed'):
        print "* " + x['title'] + " - " + x['link']


