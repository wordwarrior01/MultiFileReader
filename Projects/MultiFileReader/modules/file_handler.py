#
# Nimish Nayak
# 08-06-2017
#

# required libraries
import logging
import os 
from utils import Utils

# File Hander
# This module will handle all the file handling operations 
class FileHandler():

    # initialize the instance variables
    def __init__(self, input_file, output_file=None):
        self.input_file = input_file
        self.output_file = output_file
        logging.debug("File Hander initialized")
 
    # process the input file 
    def process_file(self):

        file_type = Utils.get_file_type(self.input_file)    

        # composition: load the appropriate parser
        # get the tuple of dictionaries for all the users in the data file
        if file_type == ".csv":
            logging.info("parsing the csv file")
            from modules.csv_parser import CsvParser  
            parser = CsvParser(self.input_file)
        elif file_type == ".yml":
            logging.info("parsing the yml file")
            from modules.yml_parser import YmlParser  
            parser = YmlParser(self.input_file)
        elif file_type == ".xml":
            logging.info("parsing the xml file")
            from modules.xml_parser import XmlParser
            parser = XmlParser(self.input_file)
        else:
            # input file is not of the neessary order
            raise IOError("File format accepted are xml,csv and yml") 
        # load the xml file 
        parser.load_file()
        # get the list of dictinary of the xml contents 
        parser.parse_file()
        # process the value 
        parser.process_file()
        # get the processed value from the parser as a string
        self.data = str(parser.get_value())              
    
    # write the output if available else print      
    def write_output(self):

        if not self.output_file:
            logging.info("Writing output to stdout as output file name not provided")
            print self.data   
        else:
            Utils.create_output_directory(self.output_file)
            with open(self.output_file, 'w') as f:
                logging.info("Writing output to the file")
                f.write(self.data)
