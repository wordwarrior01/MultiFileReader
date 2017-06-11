#
# Nimish Nayak
# 10-06-2017
#

#
# Yml Parser - Class Tests   
#

from yml_parser import YmlParser
import os

test_file = os.path.join(os.getcwd(),"Test.yml")

def test_yml_parser_with_missing_values():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""users:
  - name: Paul
    active: false
    value: 100
  - name: Ben
    active: true""")

    y = YmlParser(test_file)
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_yml_parser_with_malformed_yml():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""users:
  - name Paul
    active  false
    value 100
  - name: Ben
    active: true""")

    y = YmlParser(test_file)
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_yml_parser_with_blank_file():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("")

    y = YmlParser(test_file)
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_yml_parser_with_just_headers():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("users:")

    y = YmlParser(test_file)
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

    # delete the test file as not required 
    os.remove(test_file)