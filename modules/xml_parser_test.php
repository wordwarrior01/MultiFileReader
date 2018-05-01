<?php

#
# Nimish Nayak
# 05-07-2017
#

# Test Project to test the code base  
# Functional Test cases

# Note: Developed using PHP 7.0.18-0ubuntu0.16.04.1 (cli) ( NTS )

require_once("./modules/xml_parser.php");
require_once("./modules/utils.php");

class XmlParserTest extends PHPUnit_Framework_TestCase
{
    # Tests 

    public function testParser() {
        
        $testFile1 = Utils::joinPaths(getcwd(),"testdata","test_correct.xml"); 
        $this->xmlParser = new XmlParser($testFile1);
        # get the list of dictinary of the yml contents 
        $this->xmlParser->parseFile();
        # process the value 
        $this->xmlParser->processFile();
        # get the processed value from the parser as a string
        $this->data = $this->xmlParser->getValue();              
        $this->assertEquals($this->data, "900");

    }

    public function testParserWithIncorrectYaml() {
        
        $testFile2 = Utils::joinPaths(getcwd(),"testdata","test_incorrect.xml"); 
        $this->xmlParser = new XmlParser($testFile2);
        # get the list of dictinary of the yml contents 
        $this->xmlParser->parseFile();
        # process the value 
        $this->xmlParser->processFile();
        # get the processed value from the parser as a string
        $this->data = $this->xmlParser->getValue();              
        $this->assertEquals($this->data, 250);
    }

}

?>