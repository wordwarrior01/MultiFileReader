<?php

#
# Nimish Nayak
# 10-06-2017
#

#
# YAML Parser 
#

# required libraries
require_once("./modules/parser.php");
require_once("./modules/yaml/lib/sfYaml.php");
    
class YmlParser extends Parser {

    # initialize the instance variables
    function __construct($inputFile){
        
        # call the base class constructor
        parent::__construct($inputFile);
        echo("Yml parser initialized\n");
    }

    # parse the file using a xml parser 
    public function parseFile(){

        try {
            
            $this->doc = sfYaml::load($this->inputFile);

            #var_dump($this->doc);

            if ($this->doc['users']) {

                # we have yml data!
                # parse and create an associative array from it
                $this->data = array();

                foreach ($this->doc['users'] as $user) {

                    $dict = array('name' => $user['name'], 'active' => Utils::strToBool($user['active']), 'value' => (int)$user['value']);
                    array_push($this->data, $dict);

                }
            }
        }
        catch (Exception $e) {
            echo($e->getMessage());
        }
    }

}

?>