## Task

The aim is to create a command line tool which reads data from a file, performs simple operation on this data and stores or prints a result. Input files could have different format (csv, yml, xml), but they contain the same data. The result could be stored in a plain text file or printed on stdout. Please see the input files (located in data directory) to check the data structure.

## Logic

Run the tool from a command line and pass an input parameter and optional output parameter.
Input parameter is a path to a file that should be processed.
Output parameter is an optional path to the output file.
If the output parameter is not provided the result should be printed to stdout.

The tool should parse the input file and output the result. The result is a simple sum of value property for every active entity.

## Assumptions

File extension describes file type (*.csv, *.yml, *.xml).
User always has to pass 1 or 2 parameters - input and optionally output.

## Example 

### Python

** python main.py -i "data/file.yml" **
outputs 900

or 

** python main.py -i "file.yml" - o "result.txt" **
outputs 900

or

** python main.py --input="data/file.xml" --output="results/result.txt" **
creates results/result.txt and puts a number 900 as a content

### Php

** php main.php --input="data/file.yml" **
outputs 900

or 

** php main.php "data/file.yml" **
outputs 900

or

** php main.php --input="data/file.yml" --output="result.txt" **
creates results/result.txt and puts a number 900 as a content

## Testing 

Test cases are available in the Modules Folder along with other source code
The testing commands can be invoked from the Root Directory of the project  

### Python

For pytest you need to install pip and then do pip install pytest
Run the test suite using the following command,
pytest

### Php

PhpUnit - a Unit testing module for php code base, to install use the following command on the terminal
sudo apt-get install phpunit

Run the test suite using the following command,
phpunit -c testsuite.xml --testsuite MultiFileReaderTests

## Setup 

### Python

Windows

Install python 2.7.13 from https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz
Install Pytest from https://docs.pytest.org

Linux 

Python comes installed by default with any linux distribution like Ubuntu.

### Php

Linux 

Php 7.0 CLI - available in all the distributions, Use the following command
sudo apt-get install php7.0

XML Module - Since PHP 7 is not in the official Ubuntu PPAs, installed it through Ondřej Surý's PPA (sudo add-apt-repository ppa:ondrej/php). 
Uncomment "extension=php_xmlrpc.dll" in /etc/php/7.0/fpm/php.ini
and install php7.0-xml -> sudo apt-get install php7.0-xml
followed by restarting PHP -> sudo service php7.0-fpm restart

