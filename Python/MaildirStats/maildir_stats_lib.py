""" maildir_stats_lib.py

-- Support library for maildir_stats.py --

-- Mark J. Nenadov - 2011 - marknenadov@gmail.com --

License:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/

"""

import os, time
from datetime import date

from constants import *

class MailStats:
    """ Represents a particular users mail and abstracts away some of the unit 
    conversions and calculations

    Please note that this utilizes keyword arguments.

    ie:
    m = MailStats(user_name='joe', total_size=400000, mail_count=1029)
    print m.get_avg_mail_size('KB')
    print m.get_user_name()
    """

    total_size = 0
    mail_count = 0
    avg_mail_size = 0
    user_name = ""
    size_date_mapping = {}
    folder_depth_above = {2: 0, 3: 0}
    highest_folder_depth = 0	
    units = ""
    msgs_bigger_than_threshold = 25
	
    def __init__(self, **kws):
        """ Constructor - uses keyword arguments
        """

        assert(kws['mail_count'] != 0)

        if kws.has_key('units'): 
            self.units = kws['units']

        if kws.has_key('user_name'): 
            self.user_name = kws['user_name']

        if kws.has_key('total_size'): 
            self.total_size = kws['total_size']

        if kws.has_key('mail_count'): 
            self.mail_count = kws['mail_count']

        if kws.has_key('size_date_mapping'): 
            self.size_date_mapping = kws['size_date_mapping']

        if kws.has_key('highest_folder_depth'): 
            self.highest_folder_depth = kws['highest_folder_depth']

        if kws.has_key('folder_depth_above'): 
            self.folder_depth_above = kws['folder_depth_above']

        if kws.has_key('mail_count') and kws.has_key('total_size'):
            if kws['mail_count'] > 0:
                self.avg_mail_size = kws['total_size'] / kws['mail_count']
            else:
                self.avg_mail_size = 0

    def unit_convert(self, value):
        """ convert units
        """
    
        try:
            assert (value != 0)
        except AssertionError:
            return BAD_ENTRY
         
        try:
            assert (type(value) in (float, long, int)) 
        except AssertionError:
            return BAD_ENTRY

        return round(value / self.get_unit_factor(), 1)
    
    def get_unit_factor(self):
        """ get the current unit factor
        """

        return UNIT_FACTORS[self.units]

    def get_total_size(self, convert_units=1):
        """ Get total size
        """

        size = ""

        if convert_units:
            size = self.unit_convert(self.total_size)
        else:
            size = self.total_size

        assert(size != None)
        try:
            assert(size != 0)
        except AssertionError:
            return BAD_ENTRY
		
        return round(size, 1)
	
    def get_size_time_slice(self, days_back=0):
        """ Get the total mail storage size for e-mails received within a 
        particular time slice.

        For now this method is limited to returning a slice which extends 
        from the current time during an arbitrary number of days ago to the
        present day/time. 
        """

        assert( type(days_back) in [int]  )

        begin_time = time.time() - days_back * SECONDS_IN_A_DAY
        end_time = time.time()
        slice_size = 0

        for f_name in self.size_date_mapping.keys():
            f_size, f_date = self.size_date_mapping[f_name]

            d_begin_time = date.fromtimestamp(begin_time)
            d_end_time = date.fromtimestamp(end_time)
            d_f_date = date.fromtimestamp(f_date)
            if ( (d_f_date >= d_begin_time) and (d_f_date  <= d_end_time) ):
                slice_size += f_size
        return self.unit_convert(slice_size)

    def get_size_time_slices(self,  slice_list):
        """ Pass an list of "day agos" to get_size_time_slice() and return the 
        results
        """

        assert( len(slice_list) > 0 )

        results = {}

        for day_amount in slice_list:
            results[day_amount] = self.get_size_time_slice(day_amount)
		
        return results

    def get_mail_count(self):
        """ Get mail count
        """

        assert (self.mail_count != 0)

        return self.mail_count

    def get_avg_mail_size(self, convert_units=1):
        """ Get average mail size
        """

        if convert_units:
            s = self.unit_convert(self.avg_mail_size)
        else:
            s = self.avg_mail_size
        try:
            assert(s != None)

        except AssertionError:
            return BAD_ENTRY

        return round(s, 1)

    def get_user_name(self):
        """ Get user name
        """
        
        return self.user_name

    def get_num_msgs_bigger_than(self, threshold_size=25):
        """Get # of messages that are bigger than the threshold
        """ 
 
        if hasattr(self, 'num_msgs_bigger_than'): 
            return self.num_msgs_bigger_than

        self.msgs_bigger_than_threshold = threshold_size

        msgs = []
        for map_key, map_var in self.size_date_mapping.items():
            if (map_var[0] > (threshold_size * self.get_unit_factor())):
                msgs.append(map_key)
        return len(msgs)		

    def get_highest_folder_depth(self):
        """ get the highest folder depth they have (ie. highest level of 
        sub folders)
        """

        return self.highest_folder_depth
	
    def get_folders_above_x_levels(self, depth_num):
        """ get the number of folders that are beyond the given number of levels
        """

        return self.folder_depth_above[depth_num]
		

class AccountStatsCollection(MailStats):
    """Extends MailStats class to make it usable for managing the same 
    information about a collection of MailStats objects

    ie:
    c = AccountStatsCollection()
    c.add_item(m)
    ...
    c.update()
    print m.get_avg_mail_size('KB')
    """

    items = []
    size = 0
    count = 0
    slice_dict = {}
    units = ""
    num_msgs_bigger_than = 0

    def __init__(self, units='MB'):
        """ Constructor
        """

        self.units = units

    def add_item(self, i):	
        """ Add a MailStats object
        """

        self.items.append(i)

    def update(self):
        """Update overall counts/averages to reflect the current list of 
	MailStats items
	"""

        #global DAY_SLICES

        s = 0
        c = 0

        self.  slice_dict = {}
        for day in DAY_SLICES:
            self.slice_dict[day] = 0

        self.num_msgs_bigger_than = 0
		
        self.folder_depth_above[2] = 0
        self.folder_depth_above[3] = 0
        self.highest_folder_depth = 0

        for item in self.items:
            s += item.get_total_size()
            c += item.get_mail_count()

            self.folder_depth_above[2] += item.get_folders_above_x_levels(2)
            self.folder_depth_above[3] += item.get_folders_above_x_levels(3)
			
            if (item.highest_folder_depth > self.highest_folder_depth):
                self.highest_folder_depth = item.highest_folder_depth

            slices = item.get_size_time_slices(DAY_SLICES)
			
            for day in DAY_SLICES:
                self.slice_dict[day] += slices[day]

            threshold = item.msgs_bigger_than_threshold
            over = item.get_num_msgs_bigger_than(thershold)
            self.num_msgs_bigger_than += over

        try:
            assert (s != 0)
            self.total_size = s
        except AssertionError:
            self.total_size = BAD_ENTRY
 
        try:
            assert (c != 0)
            self.mail_count = c
        except AssertionError:
            self.total_size = BAD_ENTRY

        try:
            assert (c != 0)
            self.avg_mail_size = s / c
        except AssertionError:
            self.avg_mail_size = BAD_ENTRY
	

def analyze_maildir(mail_dir, user_name, units):
    """Walk through a maildir and return a MailStats object
    """
    global ACCOUNT_IGNORE_THRESHOLD_SIZE
    global ACCOUNT_IGNORE_THRESHOLD_COUNT
	
    total_size = 0
    mail_count = 0
	
    size_date_mapping = {}

    highest_folder_depth = 0
    folders_above_2_levels = 0
    folders_above_3_levels = 0

    for dirpath, filedirs, filenames in os.walk(mail_dir):
        not_cur_dir = dirpath.find('cur') == -1
        not_tmp_dir = dirpath.find('tmp') == -1
        not_new_dir = dirpath.find('new') == -1

        if not_cur_dir and not_tmp_dir and not_new_dir:
            dir_level = dirpath.count('.')
            if dir_level > highest_folder_depth:
                highest_folder_depth = dir_level
            if dir_level > 2:
                folders_above_2_levels += 1
            if dir_level > 3:
                folders_above_3_levels += 1
 
        for file_name in filenames:
            if (file_name.find(".mail") != -1):
                file_path = os.path.join(dirpath, file_name)
                size = os.path.getsize(file_path)

                file_ctime = os.path.getctime(file_path)
                size_date_mapping[file_name] = (size, file_ctime)
                total_size += size
                mail_count += 1

    size_of_interest = total_size > ACCOUNT_IGNORE_THRESHOLD_SIZE
    count_of_interest = mail_count > ACCOUNT_IGNORE_THRESHOLD_COUNT
    if size_of_interest and count_of_interest:
        return MailStats(total_size=total_size, mail_count=mail_count, \
			 user_name=user_name, \
			 size_date_mapping=size_date_mapping, units=units, \
			 highest_folder_depth=highest_folder_depth, \
			 folder_depth_above={2: folders_above_2_levels, \
			 3: folders_above_3_levels})

    return None
