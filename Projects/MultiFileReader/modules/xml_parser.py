#
# Nimish Nayak
# 08-06-2017
#

#
# XML Parser 
#

# required libraries
import logging
import xml.dom.minidom
from parser import Parser
from utils import Utils

class XmlParser(Parser):

    # initialize the instance variables
    def __init__(self, input_file):
    	# call the base class constructor
    	Parser.__init__(self, input_file)
        logging.debug("Xml parser initialized")

    # parse the file using a xml parser 
    def load_file(self):
        # use the parse() function to load and parse an XML file
        try:
            self.doc = xml.dom.minidom.parse(self.input_file)
        except xml.parsers.expat.ExpatError as e:
            logging.info(e)
            self.doc = None

    # parse the file using a xml parser 
    def parse_file(self):
        # get a list of XML tags from the document and create the list of dictionaries 
        if self.doc:
            users = self.doc.getElementsByTagName("user")
            logging.debug("%d users:" % users.length)
            
            for user in users:    
                
                # Default Value
                val = {"name":"","value":0,"active":False}

                # get all the tag values 
                name = user.getElementsByTagName("name")    
                value = user.getElementsByTagName("value")    
                active = user.getElementsByTagName("active")    

                if name and name[0] and name[0].firstChild:
                    val["name"] = str(name[0].firstChild.nodeValue)

                if active and active[0] and active[0].firstChild:
                    val["active"] = Utils.str_to_bool(active[0].firstChild.nodeValue)
                
                if value and value[0] and value[0].firstChild and val["active"]:
                    val["value"] = int(value[0].firstChild.nodeValue)

                self.data.append(val)
            logging.debug("data saved: %s"%self.data)
