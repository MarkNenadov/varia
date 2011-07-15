=begin
intplay_oo.rb

A IntegerFactory class to generate a random list of integers and do a 
duplicate-ignoring bit map sort on integers (given a list of integers and a max 
size). 

We do a test and compare the speed of the bit map sort with Ruby's built in 
sort() function.

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

class IntegerFactory
  attr_accessor :num_its, :max_size, :ints, :num_gen, :bit_map_sort

  def initialize(num_ints, max_size, bit_map_sort=true)
    @num_ints = num_ints
    @max_size = max_size    
    @ints = Array.new
    @num_gen = Random.new
    @bit_map_sort = bit_map_sort
  end

  def generate()
    @ints = Array.new

    Range.new(0, @num_ints-1).each do | num |
      @ints.push(@num_gen.rand(Range.new(0, @max_size-1)))
    end
  end

  def sort()
    if @bit_map_sort
      bit_map_range = Range.new(0, @max_size)
      bit_map = Array.new(@max_size, 0)

      @ints.each do | x |
        bit_map[x-1] = 1
      end

      new_ints = Array.new

      bit_map_range.each do | x |      
        if bit_map[x] == 1
          new_ints.push(x)
        end
      end
      @ints = new_ints
    else
      @ints.sort
    end
  end

  def get_results()
    return @ints
  end

end

if __FILE__ == $0
  start1 = Time.now

  AMOUNT = 1000000
  MAX_SIZE = 2000000

  integer_factory = IntegerFactory.new(AMOUNT, MAX_SIZE)
  integer_factory.generate()
  integer_factory.sort()
  result = integer_factory.get_results()

  stop1 = Time.now

  start2 = Time.now

  integer_factory = IntegerFactory.new(AMOUNT, MAX_SIZE, false)
  integer_factory.generate()
  integer_factory.sort()
  result = integer_factory.get_results()

  stop2 = Time.now

  puts "With bit_map_int_sort() it took #{(stop1 - start1)} seconds"
  puts "With Ruby's built-in sort it took #{(stop2 - start2)} seconds"
end
