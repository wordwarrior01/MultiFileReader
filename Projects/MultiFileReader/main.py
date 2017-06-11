#
# Nimish Nayak
# 10-06-2017
#

# Create a command line tool 
# which reads data from a file (csv, yml, xml), but they contain the same data 
# performs simple operation on this data 
# stores or prints a result. The result could be stored in a plain text file or printed on stdout 

# Note: Developed using Python 2.7.13

# required libraries
import logging
import os 
from optparse import OptionParser
from modules import file_handler
from modules.utils import Utils

# main function 
if __name__ == "__main__":
            
    # initialize the logger
    file_name = os.path.basename(__file__).strip().replace(".py",".log")

    # Note: Logging Level -> Production - INFO, Development - DEBUG
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', filename=file_name, level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S %p')
    
    # Set the CL options 
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 arg2"

    parser.add_option("-i", "--input", type="string",
                      help="absolute path of the input file name with file extension", 
              dest="input_file")

    parser.add_option("-o", "--output", type="string",
                      help="absolute path of the output file name with file extension", 
              dest="output_file")

    options, arguments = parser.parse_args()

    logging.info('Application Started')

    # Raise an error if the input file is missing
    if not options.input_file:
        raise ValueError("The input file is missing")

    # Debug Statements
    logging.debug("Input File %s"%options.input_file)
    logging.debug("Output File %s"%options.output_file)
    logging.debug("Arguments: %s"%arguments)

    input_file, output_file = Utils.get_absolute_path(options.input_file,options.output_file,os.getcwd())

    logging.debug("Absolute Input File %s"%input_file)
    logging.debug("Absolute Output File %s"%output_file)
    
    fh = file_handler.FileHandler(input_file, output_file)
    fh.process_file()
    fh.write_output()

    logging.info('Application Finished')