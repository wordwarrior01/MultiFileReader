<?php

#
# Nimish Nayak
# 10-06-2017
#

#
# Utils 
#
# Basic Utilities File
#

class Utils {

    # Function to process the string to boolean 
    
    public static function strToBool($strVal) {

        # echo "stringToBool received string: ", $strVal, "\n";

        $retVal = filter_var($strVal, FILTER_VALIDATE_BOOLEAN);

        return $retVal;

    }

    # Function to get the absolute path of the file

    public static function joinPaths() {
        
        $paths = array();

        foreach (func_get_args() as $arg) {
            if ($arg !== '') {
                $paths[] = $arg;
            }
        }

        return join('/', $paths);
    
    }

    # Function to get the absolute paths relative to the current working directory 

    public static function getAbsolutePath($inputFileName,$outputFileName,$currentWorkingDir=null) {

        if ($currentWorkingDir == null)
            $currentWorkingDir=getcwd();

        # Debug 
        # echo "currentWorkingDir: ", $currentWorkingDir, "\n";

        if(substr($inputFileName, 0, 4) == "data") {
            
            $inputFileName = Utils::joinPaths($currentWorkingDir,$inputFileName);                

        }
        else {

            $inputFileName = Utils::joinPaths($currentWorkingDir,"data",$inputFileName);                

        }
        
        $inputFileName = str_replace('\\', "/", $inputFileName);   # as we are on linux-ubuntu 

        if ($outputFileName != null) {

            if(substr($outputFileName, 0, 7) == "results") {
            
                $outputFileName = Utils::joinPaths($currentWorkingDir,$outputFileName);                

            }
            else {

                $outputFileName = Utils::joinPaths($currentWorkingDir,"results",$outputFileName);                

            }
            
            $outputFileName = str_replace('\\', "/", $outputFileName);   # as we are on linux-ubuntu 

        }


        # Debug 
        echo "inputFileName: ", $inputFileName, "\noutputFileName: ", $outputFileName, "\n";

        return array($inputFileName, $outputFileName);  
    }

    # Function to get the file extension 

    public static function getFileExtension($fileName=null) {

        if($fileName) {

            $ext = pathinfo($fileName, PATHINFO_EXTENSION);
            # printf("returning File extension: %s\n",$ext);
            return $ext;
        } 

        # echo("returning nothing as file_name is not provided\n");
        return null;
    }
    
    # Function to create output directory if missing

    public static function createOutputDirectory($fileName=null) {

        if ($fileName){

            # Get the directory  
            $fileDir = pathinfo($fileName)['dirname'];
            
            if (!file_exists($fileDir)) {
                printf("Creating the output directory: \n",$fileDir);
                mkdir($fileDir, 0777, true);
                return true;
            }

        }

        echo("Output directory already present\n");
        return false;
    }


    # Function to delete directory if existing

    public static function deleteDirectory($dirName) {

        if ($dirName){

            try {

                rmdir($dirName);
                printf("directory %s deleted!\n",$dirName);
                return true;
            }
            catch (Exception $e) {
                printf("Error in deleting directory %s\nError: %s\n",$dirName,$e->getMessage());
            }

        }

        return false;
    }

}
    
?>