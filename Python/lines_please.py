"""
Lines Please

INTRODUCTION

This script will traverse through whatever directory tree it is executed in and
will find source-codeish sort of file extensions and report the lines of code 
found split by type/language (via printing a dictionary for now :>).

I've personally found this handy in counting total lines of code across various
projects in my development folder (from which I push github projects, although
not all of them are on github).

AUTHOR

Mark J. Nenadov (2011)
* Essex, Ontario
* Email: <marknenadov@gmail.com> 

"""

import os
import os.path

SOURCE_EXTENSIONS = { 'C': ['.c'], 
                      'Shell': ['sh', '.bash'],
                      'Python': ['.py'],
                      'TCL' : ['.tcl'],
                      'PHP' : ['php'],
                      'Perl': ['.pl'],
                      'Ruby': ['.rb'],
                      'Java': ['.java']}

TOTALS = {}


def what_language(file_name, exts_dict):
    """ What language can we guess a filename to be
    """

    ext = os.path.splitext(file_name)[1]
    for key in exts_dict.keys():
        if ext in exts_dict[key]:
            return key
    return None

def get_source_line_count(file_path):
    """ get source line count
    """

    return len(open(file_path, 'r').readlines())

for root, dirs, files in os.walk(os.getcwd()):
    for file_name in files:
        language = what_language(file_name, SOURCE_EXTENSIONS)
        
        if language != None:
            if not language in TOTALS:
                TOTALS[language] = 0
            TOTALS[language] += get_source_lines(root + '\\' + file_name)
    
print(TOTALS)
