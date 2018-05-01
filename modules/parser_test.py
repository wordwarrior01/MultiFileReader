#
# Nimish Nayak
# 10-06-2017
#

#
# Parser - Base Class Tests   
#

from parser import Parser

def test_parser_if_abstract():
    try:
        p = Parser()
        assert(False)
    except TypeError:
        assert(True) 

def test_parser_process_file_function():
    
    class B(Parser):
        def parse_file(self):
            pass

    try:        
        B = B("test")
        B.process_file()
        assert(isinstance(B.get_value(), int))
        assert(B.get_value() == 0)
    except:
        assert(False)