<?php

#
# Nimish Nayak
# 05-07-2017
#

# Create a command line tool 
# which reads data from a file (csv, yml, xml), but they contain the same data 
# performs simple operation on this data 
# stores or prints a result. The result could be stored in a plain text file or printed on stdout 

# Note: Developed using PHP 7.0.18-0ubuntu0.16.04.1 (cli) ( NTS )

# main invocation 
require_once("./modules/utils.php");
require_once("./modules/file_handler.php");

echo 'Application Started', "\n";

# $ php script.php --input="data/file.xml" --output="results/result.txt"
$longopts = array(
    "input::",     // Optional value
    "output::"     // Optional value
);

$params = getopt("", $longopts);

# no long options provided 
if(!count($params)) {

	# $ php script.php data/file.yml
	switch($argc){

		case 3:
			$output = $argv[2];
			$input = $argv[1];
			break;
		
		case 2:
			$input = $argv[1];
			$output = null;
			break;

		default:
			$output = null;
			$input = null;

	}
}
else {

	$input = $params['input'];
	$output = $params['output'];

}

# Debug
printf("Command Line Parameters %s\n%s\n",$input,$output);

# Raise an error if the input file is missing
# if output file is provided, check if the file extension is there or not 
if (($input == null) || (($output != null) && (Utils::getFileExtension($output)==null))) {

	echo "input file name not provided\n";
	exit(1);

}

# Check if file extension is provided or not
if(Utils::getFileExtension($input)==null) {
	echo "no file extensions provded \n";
	exit(1);
}

# Test
# echo Utils::strToBool("Nimish""");
# echo Utils::getFileExtension("Nimish.txt");
# echo Utils::createOutputDirectory("/home/nimish/Nimish.txt");

$ioParams = Utils::getAbsolutePath($input,$output);
$inputFile = $ioParams[0];
$outputFile = $ioParams[1];
# Print Statement available in the class::function.
# printf("Relative Paths %s\n%s\n",$inputFile,$outputFile);

$fh = new FileHandler($inputFile, $outputFile);
$fh->processFile();
$fh->writeOutput();

echo 'Application Finished', "\n"

?>
