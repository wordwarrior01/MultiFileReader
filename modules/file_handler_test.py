#
# Nimish Nayak
# 10-06-2017
#

# required libraries
from file_handler import FileHandler

# File Hander
# This module will handle all the file handling operations 

def test_file_handler_non_std_file_types():

    try:
        fh = FileHandler("Data/Test.psv")
        fh.process_file()
        assert(False)
    except IOError:
        assert(True)