#
# Nimish Nayak
# 10-06-2017
#

#
# Xml Parser - Class Tests   
#

from xml_parser import XmlParser
import os

test_file = os.path.join(os.getcwd(),"Test.xml")

def test_xml_parser_with_missing_values():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""<?xml version="1.0" encoding="UTF-8" ?>
<users>
    <user>
        <name>John</name>
        <active>true</active>
    </user>
    <user>
        <name>Mark</name>
        <active>false</active>
        <value>250</value>
    </user>
</users>""")

    y = XmlParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_xml_parser_with_malformed_xml():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""<?xml version="1.0" encoding="UTF-8" ?>
<users>
    <user
        <name>John</name>
        <active>true</active>
    /user>
    <user>
        <name>Mark</name>
        active>false</active>
        <value>250</value
    </user>
</users>""")

    y = XmlParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)


def test_xml_parser_with_blank_file():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("")

    y = XmlParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_xml_parser_with_no_child_nodes():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""<?xml version="1.0" encoding="UTF-8" ?>
<users>""")

    y = XmlParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

def test_xml_parser_with_xml_dtd():
    
    global test_file    

    # value missing
    with open(test_file,"w")as f:
        f.write("""<?xml version="1.0" encoding="UTF-8" ?>""")

    y = XmlParser(test_file)
    y.load_file()
    y.parse_file()
    y.process_file()
    assert(y.get_value() == 0)

    # delete the test file as not required 
    os.remove(test_file)