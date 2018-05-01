<?php

#
# Nimish Nayak
# 10-06-2017
#

#
# FileHandler 
#

require_once("./modules/utils.php");

# File Hander
# This module will handle all the file handling operations 

class FileHandler {

    # initialize the instance variables
    function __construct($inputFile, $outputFile) {
        
        $this->inputFile = $inputFile;
        $this->outputFile = $outputFile;
        echo("File Hander initialized\n");

    }

    # process the input file 
    public function processFile() {

        $ext = Utils::getFileExtension($this->inputFile);    

        # composition: load the appropriate parser
        # get the tuple of dictionaries for all the users in the data file
        switch($ext){

            case "csv":
                echo("parsing the csv file\n");
                require_once("./modules/csv_parser.php");
                $parser = new CsvParser($this->inputFile);
                break;

            case "yml":
                echo("parsing the yml file\n");
                require_once("./modules/yml_parser.php");
                $parser = new YmlParser($this->inputFile);
                break;

            case "xml":
                echo("parsing the xml file\n");
                require_once("./modules/xml_parser.php");
                $parser = new XmlParser($this->inputFile);
                break;

            default:
                echo("file type not supported\n");
                return null;
        }

        # read file contents 
        $parser->parseFile();
        # process file contents based on certain criteria 
        $parser->processFile();
        # return parsed value
        $this->data = $parser->getValue();              
    
    }

    # write the output if available else print      
    public function writeOutput() {

        if($this->outputFile != null) {
            Utils::createOutputDirectory($this->outputFile);
            echo("Writing output to the file\n");
            $file = fopen($this->outputFile,"w");
            var_dump($this->data);
            fwrite($file,$this->data);
            fclose($file);
        }
        else
            printf("Writing output to stdout as output file name not provided\n%s\n",$this->data);  
    }

}

?>