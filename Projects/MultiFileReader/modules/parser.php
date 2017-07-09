<?php

#
# Nimish Nayak
# 10-06-2017
#

#
# Parser - Base Class  
#
 
abstract class Parser {

    # initialize the instance variables
    function __construct($inputFile) {
        $this->inputFile = $inputFile;
        $this->data = array();
        $this->value = 0;
    }

    # enforce the extending class to define it  
    abstract protected function parseFile();

    # process value from the input 
    public function processFile(){
        
        # list comprehension
        echo("Processing the file contents\n");

        if($this->data) {   # array of associative arrays 
            
            foreach ($this->data as $dict) {  # associative array 

                # check if it is an associative array or not
                
                if(isset($dict['active']) && isset($dict['value']) && $dict['active']) {

                    $this->value += $dict['value'];

                }    
            }       
        }

    }

    # return to the calling convention 
    public function getValue(){
        $val = strVal($this->value);
        printf("Processed value is: %s\n",$val);
        return $val;
    }
}

?>