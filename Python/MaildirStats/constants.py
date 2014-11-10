""" mailstats.py

 Iterates through all "Maildir" directories that are located in users home directories
 and calcuates various useful stats about their mail and puts it out into a csv file 

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

CSV_OUT_FILE = "mailstats.csv"
HOME_DIRS = ['/usr/home2/', '/home/']
USERS_TO_IGNORE = ['chrisw', 'nszydlek', 'phila', 'shawnm', 'bdinkleman', 'rjackson', 'ddtps', 'rclaeys', 'ggirard', 'dsutts', 'lraymond', 'erics', 'rgirard', 'student', 'resumes', 'jscott', 'kboakes', 'accounting', 'mkobelsky', 'mletourneau', 'lracine', 'lmontgomery', 'rickc']
ACCOUNT_IGNORE_THRESHOLD_SIZE = 50000 # bytes
ACCOUNT_IGNORE_THRESHOLD_COUNT = 50 # emails
BAD_ENTRY = 0.0

DAY_SLICES = (365, 100, 60, 30, 15)
SECONDS_IN_A_DAY = 86400
UNIT_FACTORS = {'': 1.0, 'KB': 1024.0, 'MB': 1048576.0}
