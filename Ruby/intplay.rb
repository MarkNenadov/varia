=begin
intplay.rb

A couple fun integer functions, one to do a duplicate-ignoring bit map
sort on integers (given a list of integers and a max size). The other to
generate random integers (given amount and max size)

We do a test and compare the speed with Ruby's built-in sort() function. 
On my computer with Ruby 2.1 and 2 million integers, the bit map sort 
beats out the built-in Ruby sort by about 0.2 seconds.


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
=end

def bit_map_int_sort(ints, largest_value)
   bit_map_range = Range.new(0, largest_value)
   bit_map = Array.new(largest_value, 0)

   ints.each do | x |
      bit_map[x-1] = 1
   end

   new_ints = Array.new

   bit_map_range.each do | x |
      if bit_map[x] == 1
         new_ints.push(x)
      end
   end
   return new_ints
end

def get_random_ints(num_ints, max_size)
   ints = Array.new
   num_gen = Random.new

   Range.new(0, num_ints-1).each do | num |
      ints.push(num_gen.rand(Range.new(0, max_size-1)))
   end
   return ints
end

if __FILE__ == $0
  start1 = Time.now

  AMOUNT = 2000000
  MAX_SIZE = 2000000

  result = bit_map_int_sort(get_random_ints(AMOUNT, MAX_SIZE), MAX_SIZE)

  stop1 = Time.now

  start2 = Time.now

  get_random_ints(AMOUNT, MAX_SIZE).sort

  stop2 = Time.now

  puts "With bit_map_int_sort() it took #{(stop1 - start1)} seconds"
  puts "With Ruby's built-in sort it took #{(stop2 - start2)} seconds"
end
