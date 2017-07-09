<?php

#
# Nimish Nayak
# 10-06-2017
#

#
# XML Parser 
#

# Note: To get the XML Module - 

# Since PHP 7 is not in the official Ubuntu PPAs, installed it through Ondřej Surý's PPA (sudo add-apt-repository ppa:ondrej/php). 

# uncomment the following line in /etc/php/7.0/fpm/php.ini
# extension=php_xmlrpc.dll

# and install php7.0-xml:
# sudo apt-get install php7.0-xml

# restart PHP:
# sudo service php7.0-fpm restart

# required libraries
require_once("./modules/utils.php");
require_once("./modules/parser.php");

class XmlParser extends Parser {

    # initialize the instance variables
    function __construct($inputFile){
        
        # call the base class constructor
        parent::__construct($inputFile);
        echo("Xml parser initialized\n");
    }

    # load the file using an xml parser
    private function loadFile(){

        # read the whole file into a string
        $myXMLData = file_get_contents($this->inputFile);

        # string -> xml
        $this->doc = simplexml_load_string($myXMLData);
        
        # Debug 
        # var_dump($this->doc);

        if ($this->doc === false) {
            echo "Failed loading XML:\n";
            foreach(libxml_get_errors() as $error) {
                echo $error->message, "\n";
            }
        }
    }
        
    # parse the file using a xml parser 
    public function parseFile() {

        $this->loadFile();

        if ($this->doc->user) {

            # we have xml data!
            # parse and create an associative array from it
            $this->data = array();

            foreach ($this->doc->user as $user) {

                $dict = array('name' => $user->name, 'active' => Utils::strToBool($user->active), 'value' => (int)$user->value);
                array_push($this->data, $dict);

            }

        }

    }
}

?>