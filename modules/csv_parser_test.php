<?php

#
# Nimish Nayak
# 05-07-2017
#

# Test Project to test the code base  
# Functional Test cases

# Note: Developed using PHP 7.0.18-0ubuntu0.16.04.1 (cli) ( NTS )

require_once("./modules/csv_parser.php");
require_once("./modules/utils.php");

class CsvParserTest extends PHPUnit_Framework_TestCase
{
    # Tests 

    public function testParser() {
        
        $testFile1 = Utils::joinPaths(getcwd(),"testdata","test_correct.csv"); 
        $this->csvParser = new CsvParser($testFile1);
        # get the list of dictinary of the yml contents 
        $this->csvParser->parseFile();
        # process the value 
        $this->csvParser->processFile();
        # get the processed value from the parser as a string
        $this->data = $this->csvParser->getValue();              
        $this->assertEquals($this->data, "900");

    }

    public function testParserWithIncorrectYaml() {
        
        $testFile2 = Utils::joinPaths(getcwd(),"testdata","test_incorrect.csv"); 
        $this->csvParser = new YmlParser($testFile2);
        # get the list of dictinary of the yml contents 
        $this->csvParser->parseFile();
        # process the value 
        $this->csvParser->processFile();
        # get the processed value from the parser as a string
        $this->data = $this->csvParser->getValue();              
        $this->assertEquals($this->data, 0);
    }

}

?>