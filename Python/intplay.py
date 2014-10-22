"""

intplay.py

A couple fun integer functions, one to do a duplicate-ignoring bit map
sort on integers (given a list of integers and a max size). The other to
generate random integers (given amount and max size)

In __main__ we do a test and compare the speed with Python's built in
sort() function.

(On my computer at least) With Python 2.7, bit_map_int_sort()
tends to beat out Python sort() by about 1 second on a list of 2mil
integers. On Python 3.4, the difference is greater--about 1.5 seconds.

AUTHOR

Mark J. Nenadov (2011-2014)
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

import random
import time

def bit_map_int_sort(ints, largest_value):
    """ bit_map_int_sort()

    Sort a list of integers (ignoring duplicates) using a bit map and return
    the results. Based on the bit map sort that is discussed in Programing
    Pearls by Jon Bentley

    """
    bit_map = [0]*largest_value
    bit_map_range = range(largest_value)

    # generate bit map
    for x in ints:
        bit_map[x-1] = 1

    # generate and return sorted list
    new_ints = []
    for x in bit_map_range:
        if bit_map[x] == 1:
            new_ints.append(x)

    return new_ints

def get_random_ints(num, max_size):
    """ get_random_ints ()

    return n integers with a maximum size of n
    """

    ints = []
    for x in range(num-1):
        ints.append(random.randint(0,max_size-1))

    return ints

if __name__ == "__main__":
    # we'll work with 2mil integers that have values no bigger than 2mil
    AMOUNT = 2000000
    MAX_SIZE = 2000000

    # try bit_map_int_sort()
    start1 = time.time()
    result = bit_map_int_sort(get_random_ints(AMOUNT, MAX_SIZE), MAX_SIZE)
    stop1 = time.time()

    # try the same thing with Python's built in sort()
    start2 = time.time()
    get_random_ints(AMOUNT, MAX_SIZE).sort()
    stop2 = time.time()
    
    print( "With bit_map_int_sort() it took " + str(stop1-start1) \
            + " seconds to sort " + str(AMOUNT) + \
            " integers that have values up to " + str(MAX_SIZE))
    print( "With Python's built-in sort() it took " + str(stop2-start2) + \
            " seconds to sort " + str(AMOUNT) + \
            " integers that have values up to " + str(MAX_SIZE))
