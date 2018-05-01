#
# Nimish Nayak
# 10-06-2017
#

#
# Parser - Base Class  
#

# required libraries
import logging
from abc import ABCMeta, abstractmethod
 
class Parser():

    __metaclass__ = ABCMeta

    # initialize the instance variables
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = []
        self.value = 0

    # parse the file using a xml parser
    # to be overridden  
    def load_file(self):
        # use the parse() function to load and parse an XML file
        self.doc = None

    # parse the file using a xml parser
    # Has to be to be overridden 
    @abstractmethod
    def parse_file(self):
        pass

    # process value from the input 
    def process_file(self):
        # list comprehension
        logging.debug("Processing the xml file")
        if self.data:
            for k in self.data:
                if type(k)==dict and len(k.keys())==3 and "active" in k and "value" in k and k["active"]:
                    self.value += k["value"]            
        #self.value += sum([k["value"] for k in self.data if k["active"]])
        
    # return to the calling convention 
    def get_value(self):
        logging.debug("Processed value is: %s"%str(self.value))
        return self.value