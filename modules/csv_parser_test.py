#
# Nimish Nayak
# 10-06-2017
#

#
# Csv Parser - Class Tests   
#

from csv_parser import CsvParser
import os

test_file = os.path.join(os.getcwd(),"Test.csv")

def test_csv_parser_with_missing_values():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""name,active,value
John,true,
Mark,true,
Paul,false,100
Ben,true,150
""")

    y = CsvParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 150)

def test_csv_parser_with_non_csv_values():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""name,active,value
John true 
Mark true 
Paul false 100
Ben true 150
""")

    y = CsvParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_csv_parser_with_blank_file():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("")

    y = CsvParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_csv_parser_with_no_child_nodes():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""name,active,value""")

    y = CsvParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

    # delete the test file as not required 
    os.remove(test_file)