del *.py~
del *.txt~
del *.pyc
del *.bat~

c:\python27\python c:\python27\lib\pydoc.py -w maildir_stats.py
c:\python27\python c:\python27\lib\pydoc.py -w maildir_stats_lib
c:\python27\python c:\python27\lib\pydoc.py -w constants

move maildir_stats.html api_doc
move maildir_stats_lib.html api_doc
move constants.html api_doc
