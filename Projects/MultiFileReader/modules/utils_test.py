#
# Nimish Nayak
# 10-06-2017
#

#
# Utils Unit Test  
#

from utils import Utils 
import os 

# Test the str_to_bool function

def test_str_to_bool_with_no_args():
	assert(Utils.str_to_bool(None) == None)
	assert(Utils.str_to_bool("") == None)

def test_str_to_bool_with_incorrect_args():
	assert(Utils.str_to_bool("Test") == "Test")

def test_str_to_bool_with_incorrect_args_type():
	assert(Utils.str_to_bool(1) == None)

def test_get_file_type_with_no_args():
	assert(Utils.get_file_type(None) == None)
	assert(Utils.get_file_type("") == None)

def test_get_file_type_with_no_file_ext():
	assert(Utils.get_file_type("Test") == "")

def test_get_file_type_with_file_ext():
	assert(Utils.get_file_type("Test.txt") == ".txt")
	assert(Utils.get_file_type("Test/Test.txt") == ".txt")

def test_create_output_directory_with_no_args():
	assert(Utils.create_output_directory(None) == None)

def test_create_output_directory_with_no_existing_dir():
	assert(Utils.create_output_directory("data/data1/test.txt") == True)

def test_create_output_directory_with_existing_dir():
	assert(Utils.create_output_directory("data/data1/test.txt") == True)
	os.rmdir(os.path.join(os.getcwd(),"data/data1"))

def test_get_absolute_path_with_no_args():
	assert(Utils.get_absolute_path(None,None) == (None,None))

def test_get_absolute_path_with_input_args():
	assert(Utils.get_absolute_path("",None) == ("",None))

def test_get_absolute_path_with_input_file():
	path = os.path.join(os.getcwd(),"data","test.xml")
	assert(Utils.get_absolute_path("test.xml",None) == (path,None))
	assert(Utils.get_absolute_path("data/test.xml",None) == (path,None))

def test_get_absolute_path_with_output_file():
	path = os.path.join(os.getcwd(),"results","test.xml")
	assert(Utils.get_absolute_path(None,"test.xml") == (None,path))
	assert(Utils.get_absolute_path(None,"results/test.xml") == (None,path))