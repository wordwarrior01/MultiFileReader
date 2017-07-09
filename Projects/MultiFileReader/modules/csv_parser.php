<?php

#
# Nimish Nayak
# 10-06-2017
#

#
# CSV Parser 
#

require_once("./modules/utils.php");
require_once("./modules/parser.php");

class CsvParser extends Parser {

    # initialize the instance variables
    function __construct($inputFile){
        
        # call the base class constructor
        parent::__construct($inputFile);
        echo("Csv parser initialized\n");
    }
    
    # parse the file using a csv parser 
    public function parseFile(){

        $fp = fopen($this->inputFile,"r");

        $this->data = array();

        while (!feof($fp)) {

            $lineArray = fgetcsv($fp);

            # create an associative array from the line 
            # name,active,value
            # John,true,500

            $dict = array("name" => $lineArray[0], "active" => Utils::strToBool($lineArray[1]), "value" => (int)$lineArray[2]);
            array_push($this->data, $dict);

        }

        fclose($fp);
        # var_dump($this->data);
    }

}

?>