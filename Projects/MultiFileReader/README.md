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

** python main.py -i "data/file.yml" **
outputs 900

or 

** python main.py -i "file.yml" - o "result.txt" **
outputs 900

or

** python main.py --input="data/file.xml" --output="results/result.txt" **
creates results/result.txt and puts a number 900 as a content

## Setup 

Windows

Install python 2.7.13 from https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz
Install Pytest from https://docs.pytest.org

Linux 

Python should be pre-installed with any distribution like Ubuntu
For pytest you need to install pip and then do pip install pytest
