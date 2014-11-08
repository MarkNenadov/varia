#
# rsspriority.rb - v1.0
#
# - Code that facilitates the prioritization of RSS feed content based on keyword scores. 
#   It displays RSS feed items from highest score on the top to lowest on the bottom. It
#   also ignores items that have a score less than an arbitrary number (-400 default).
#   It also should be noted that a hit in the title doubles the score applied for
#   that keyword find.
#
# The Key Classes:
#
# RSSContentPriorityList (class)
# - initialized with a simple array of rss source URIs and a keyword merit associative array (with integers negative or positive for each keyword)
# - can be used to return list of RSS contenet from rss source URIs sorted based on keyword merit rating
#
# HtmlFormatter, etc. (class)
# - initialized with a RSSContentPriorityList object
# - handles presentation of prioritized rss content in HTML, etc.
#
# by Mark J. Nenadov - March 15, 2011
#
# License:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.

require 'rss/1.0'
require 'rss/2.0'
require 'open-uri'

require 'constants.rb'


class RSSContentItem
	#@title
	#@desc
	#@channel_desc
	#@score
	#@url

	def initialize(title, desc, channel_desc, url)
		@title = title
		@desc = desc
		@url = url
		@channel_desc = channel_desc
		@score = 0
	end

	def get_content(strip_html_tags=0)
		if strip_html_tags
			return @desc.gsub(/<\/?[^>]*>/, " ")
		end
		return @desc
	end

	def get_title()
		return @title
	end

	def get_channel_desc()
		return @channel_desc
	end

	def get_url()
		return @url
	end

	def get_score()
		return @score
	end

	def adjust_score(s)
		@score += s
	end
end

class RSSContentPriorityList
	#@source_list
	#@keyword_merit
	#@content_items
	#@ignore_point

	def initialize(source_list, keyword_merit)
		@source_list = source_list
		@keyword_merit = keyword_merit
		@content_items = Array.new
		set_ignore_score(-400) # any entries with less than this score will be ignored
		generate_content()
	end

	def get_priority(kw)
		return @keyword_merit[kw]
	end

	def set_ignore_score(s)
		@ignore_score = s
	end

	def generate_content()
		@source_list.each { |rss_feed|
			content = ''
			open(rss_feed) do |s| content = s.read end
			rss = RSS::Parser.parse(content, false)

			rss.items.each { |entry|
				@content_items.push RSSContentItem.new( entry.title, entry.description, rss.channel.description , entry.link )
			}
		}
	end

	def sort_content_by_score(c)
		return c.sort_by {|a| a.get_score() }.reverse
	end


	def get_rated_content
		rated_content = Array.new
		@content_items.each { |content|
			for kw in @keyword_merit.keys
				if content.get_content().downcase.include?(kw) or content.get_title().downcase.include?(kw)
					score_change = @keyword_merit[kw]
					if content.get_title().downcase.include?(kw)
						score_change = score_change * 2
					end
					content.adjust_score(score_change)

				end
			end
			if content.get_score() > @ignore_score
				rated_content.push content
			end
		}
		return sort_content_by_score(rated_content)

	end

	private :generate_content
	private :sort_content_by_score
end

class GenericPrinter
	#@priority_list
	
	def initialize(p)
		set_priority_list(p)
	end

	def set_priority_list(p)
		@priority_list = p
	end

	def display()
		s = ""
		@priority_list.get_rated_content().each { | content |
			s += get_item_output(content)
		}
		return s
	end

	def get_item_output(i)
	end


end

class HtmlPrinter < GenericPrinter

	def initialize(p)
		super(p)
	end

	def set_priority_list(p)
		super(p)
	end

	def display()
		puts super()
	end

	def get_item_output(i)
		super(i)
		
		s = "<h2><a href='"+i.get_url()+"'>" + i.get_title + "</a></h2>\n\n<p>"
		s += "Source: <b>" + i.get_channel_desc()
		s += "</b><br />Score: <b>" + i.get_score().to_s()
		s += "</b><br />Url: <a href='"+ i.get_url() + "'>" + i.get_url() +"</a>"
		s += "</p>\n\n<p>" + i.get_content() + "</p>"
		
	end

end

class TextPrinter < GenericPrinter
	def initialize(p)
		super(p)
	end

	def set_priority_list(p)
		super(p)
	end

	def display()
		puts super()
	end

	def get_item_output(i)
		super(i)

		s = "Title: " + i.get_title() + "\n\n\n"
		s += "Source: " + i.get_channel_desc() + "\n\n"
		s += "Desc: " + i.get_content(strip_html_tags=1) + "\n" 
		s += "Url: " + i.get_url() + "\n"
		s += "Score: " + i.get_score().to_s() + "\n"
		s += "\n\n\n"

		return s
	end

end

# A simplied sample implementation (covers core functionality, but not all features)

# Generate Rated, Sorted Content

RSSContent = RSSContentPriorityList.new(source_list, keyword_merit)

# Print HTML Output

f = HtmlPrinter.new( RSSContent )   # use TextPrinter with the same code for plain text
results = f.display()

if not results.nil?
	puts results
end

