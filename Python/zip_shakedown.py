"""Take all zip files in a given path and list their contents in a text file

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

import os.path
import zipfile

WORKING_FOLDER = "C:\\archives\\"

def is_zip(working_file):
    """ Check extension to see if it zip
    """

    if os.path.splitext(working_file)[1] == '.zip':
        return 1
    return 0

def ignore_case(left, right):
    """ A sort function to sort ignoring case
    """
    if left.upper < right.upper:
        return -1
    return 1

WORKING_FOLDER_CONTENTS = os.listdir(WORKING_FOLDER)

ZIP_REPORT = open("report.txt", "w")

for zip_file_name in WORKING_FOLDER_CONTENTS:
    if is_zip(zip_file_name):
        ZIP_REPORT.write("\n" + zip_file_name + "...\n")
        try:
            zip_file = zipfile.ZipFile(WORKING_FOLDER + zip_file_name)
            zip_file.namelist()
        except zipfile.BadZipfile:
            ZIP_REPORT.write(".. Can't open it\n\n")
        except:
            ZIP_REPORT.write(".. Can't open it\n\n")

    else:
        zip_contents = zip_file.namelist()
        zip_contents.sort(ignore_case)

        for zip_content in zip_contents:
            ZIP_REPORT.write(zip_content + "\n")
        zip_file.close(

