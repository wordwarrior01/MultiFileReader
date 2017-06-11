#
# Nimish Nayak
# 10-06-2017
#

#
# CSV Parser 
#

# required libraries
import logging
import csv
from parser import Parser
from utils import Utils

class CsvParser(Parser):

    # initialize the instance variables
    def __init__(self, input_file):
        # call the base class constructor
        Parser.__init__(self, input_file)
        logging.debug("Csv parser initialized")

    # parse the file using a csv parser 
    def parse_file(self):
        # get a list of CSV tags from the document and create the list of dictionaries 
        with open(self.input_file, "rb") as f:
            users = [row for row in csv.reader(f)][1:]    
        logging.debug("%d users:" % len(users))
        for user in users:
            
            # default values 
            val = {"name":"","active":False,"value":0}
            
            # check if csv 
            if len(user) == 3:
                if user[0]:
                    val["name"] = user[0]
                if user[1]:
                    val["active"] = Utils.str_to_bool(user[1])
                if user[2]:
                    val["value"] = int(user[2])
            self.data.append(val)
        logging.debug("data saved: %s"%self.data)