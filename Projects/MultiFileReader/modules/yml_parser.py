#
# Nimish Nayak
# 08-06-2017
#

#
# YAML Parser 
#

# required libraries
import logging
import yaml
from parser import Parser 

class YmlParser(Parser):

    # initialize the instance variables
    def __init__(self, input_file):
    	# call the base class constructor
    	Parser.__init__(self, input_file)
        logging.debug("Yml parser initialized")

    # parse the file using a xml parser 
    def parse_file(self):
		with open(self.input_file, "r") as f:
			data = yaml.load(f)
			if data and "users" in data:
				self.data = data["users"]