""" mailstats.py

 Iterates through all "Maildir" directories that are located in users 
 home directories and calcuates various useful stats about their mail 
 and puts it out into a csv file 

 -- Mark J. Nenadov - 2011 - marknenadov@gmail.com

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
    along with this program.  If not, see <http://www.gnu.org/licenses

"""


import os,  csv, time

from constants import *

from maildir_stats_lib import AccountStatsCollection
from maildir_stats_lib import analyze_maildir

START_TIME = time.time()

CSV_WRITER = csv.writer(open(CSV_OUT_FILE, 'wb'), delimiter=',', \
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
CSV_CONTENT = ["User Name", "Total Acct Size", "Emails (#)", "Avg Mail Size", \
               "Msgs > 25 MB", "Highest Folder Level", "Folders > 2 Levels", \
	       "Folders > 3 Levels"]

for day_amount in DAY_SLICES:
    CSV_CONTENT.append("Size last " + str(day_amount) + " d")

CSV_WRITER.writerow(CSV_CONTENT)

USER_FOLDERS = []
STATS_COLLECTION = AccountStatsCollection()

for home_dir in HOME_DIRS:
    print("Analyzing Maildir: " + home_dir)
    for d in os.listdir(home_dir):
        if os.path.isdir(home_dir + d):
            print("..." + home_dir + d)
            USER_FOLDERS.append([home_dir + d, d])

for user_dir, user_name in USER_FOLDERS:
    if user_name not in USERS_TO_IGNORE:
        if os.path.isdir(user_dir + "/Maildir"):
            m = analyze_maildir(user_dir + "/Maildir", user_name, 'MB')
            if m is not None:
                slice_sizes = m.get_size_time_slices(DAY_SLICES)
                STATS_COLLECTION.add_item(m)

                M_USER = m.get_user_name()
                M_TOTAL_SIZE = str(m.get_total_size())
                M_MAIL_COUNT = str(m.get_mail_count())
                M_AVG_MAIL_SIZE =  str(m.get_avg_mail_size())
                M_MSGS_BIGGER_THAN = str(m.get_num_msgs_bigger_than())
                M_HIGHEST_DEPTH = m.get_highest_folder_depth()
                M_DEPTH_GT_2 = m.get_folders_above_x_levels(2)
                M_DEPTH_GT_3 = m.get_folders_above_x_levels(3)

                CSV_CONTENT = [ M_USER,  M_TOTAL_SIZE, M_MAIL_COUNT, \
				M_AVG_MAIL_SIZE, M_MSGS_BIGGER_THAN, \
				M_HIGHEST_DEPTH, M_DEPTH_GT_2, M_DEPTH_GT_3]
				
                for day_amount in DAY_SLICES:
                    CSV_CONTENT.append(slice_sizes[day_amount])

                CSV_WRITER.writerow(CSV_CONTENT)
STATS_COLLECTION.update()

print("Outputting CSV content to " + CSV_OUT_FILE)

SC_TOTAL_SIZE = STATS_COLLECTION.get_total_size(0)
SC_MAIL_COUNT = STATS_COLLECTION.get_mail_count()
SC_AVG_MAIL_SIZE = STATS_COLLECTION.get_avg_mail_size(0)
SC_FOLDERS_ABOVE_3_LEVELS = STATS_COLLECTION.get_folders_above_x_levels(3)
SC_FOLDERS_ABOVE_2_LEVELS = STATS_COLLECTION.get_folders_above_x_levels(2)
SC_MSGS_BIGGER_THAN = STATS_COLLECTION.get_num_msgs_bigger_than()
SC_HIGHEST_DEPTH = STATS_COLLECTION.get_highest_folder_depth()

CSV_CONTENT = ["Totals", SC_TOTAL_SIZE, SC_MAIL_COUNT, SC_AVG_MAIL_SIZE, \
               SC_MSGS_BIGGER_THAN, SC_HIGHEST_DEPTH, \
	       SC_FOLDERS_ABOVE_2_LEVELS, SC_FOLDERS_ABOVE_3_LEVELS]

for day_amount in DAY_SLICES:
    CSV_CONTENT.append(STATS_COLLECTION.slice_dict[day_amount])


CSV_WRITER.writerow(CSV_CONTENT)

TOTAL_ITEMS = len(STATS_COLLECTION.items)
print("Done. Processed and output information about " + str(TOTAL_ITEMS) + \
      " accounts")

STOP_TIME = time.time()

print("Execution time (seconds): " + str(STOP_TIME - START_TIME))
