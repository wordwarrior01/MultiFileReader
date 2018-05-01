#
# Nimish Nayak
# 10-06-2017
#

#
# Utils 
#
# Basic Utilities File
#

# required libraries
import logging
import os 

class Utils():

    # Function to process the string to boolean 
    
    @staticmethod
    def str_to_bool(string_val):

        logging.debug("str_to_bool received string: %s"%string_val)

        if not string_val or not isinstance(string_val, basestring):
            logging.debug("returning None as string_val is not provided or is incorrect")
            return None

        string_val = string_val.capitalize()

        if string_val == "True":
            logging.debug("returning boolean True")
            return True 
        elif string_val == "False":
            logging.debug("returning boolean False")
            return False
        else:
            logging.debug("returning as is as string_val cannot be processed")
            return string_val

    # Function to get the file extension 

    @staticmethod 
    def get_file_type(file_name):

        if not file_name:
            logging.debug("returning None as file_name is not provided")
            return None
        
        file_ext = os.path.splitext(file_name)[1]
        logging.debug("returning File extension: %s"%file_ext)
        return file_ext

    # Function to create output directory if missing

    @staticmethod 
    def create_output_directory(file_name):
        
        if not file_name:
            return None

        file_dir = os.path.dirname(file_name)
        if not os.path.exists(file_dir):
            logging.debug("Creating the output directory")
            os.makedirs(file_dir)
        logging.debug("Output directory already present")
        return True

    # Function to get the absolute paths relative to the current working directory 
    
    @staticmethod
    def get_absolute_path(input_file_name,output_file_name,curr_working_dir=os.getcwd()):
        
        root = curr_working_dir

        if input_file_name:
            if not input_file_name.startswith("data"):
                input_file_name = os.path.join(root,"data",input_file_name)
            else:
                input_file_name = os.path.join(root,input_file_name)
            input_file_name = input_file_name.replace('\\',"/")   # as we are on linux-ubuntu 
                    
        if output_file_name:
            if not output_file_name.startswith("results"):
                output_file_name = os.path.join(root,"results",output_file_name)
            else:
                output_file_name = os.path.join(root,output_file_name)
            output_file_name
            output_file_name = output_file_name.replace('\\',"/")   # as we are on linux-ubuntu 
                    
        return input_file_name, output_file_name