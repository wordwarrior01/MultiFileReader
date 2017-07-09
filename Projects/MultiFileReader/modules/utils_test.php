<?php

#
# Nimish Nayak
# 05-07-2017
#

# Test Project to test the code base  
# Functional Test cases

# Note: Developed using PHP 7.0.18-0ubuntu0.16.04.1 (cli) ( NTS )

require_once("./modules/utils.php");

class UtilsTest extends PHPUnit_Framework_TestCase
{
    # Tests 

    public function teststrToBoolWithNull() {

        $retVal = Utils::strToBool(Null);
        $this->assertEquals($retVal, false);

    }

    public function teststrToBoolWithStringDataType() {

        $retVal = Utils::strToBool("Nimish");
        $this->assertEquals($retVal, false);

    }

    public function teststrToBoolWithIntegerDataType() {

        $retVal = Utils::strToBool(9);
        $this->assertEquals($retVal, false);

    }

    public function testJoinPathsWithNull() {

        $retVal = Utils::joinPaths(Null);
        $this->assertEquals($retVal, '');

    }

    public function testJoinPathsWithMultipleNulls() {

        $retVal = Utils::joinPaths(Null,Null);
        $this->assertEquals($retVal, '/');

    }

    public function testJoinPathsWithWrongDataType() {

        $retVal = Utils::joinPaths(8,6,7);
        $this->assertEquals($retVal, '8/6/7');

    }

    public function testgetAbsolutePathWithOnlyInput() {

        $retVal = Utils::getAbsolutePath('test.csv',Null);
        $checkVal = array(Utils::joinPaths(getcwd(),'data','test.csv'),Null);
        $this->assertEquals($retVal, $checkVal);

    }

    public function testgetAbsolutePathWithNull() {

        $retVal = Utils::getAbsolutePath(Null,Null,Null);
        $checkVal = array(Utils::joinPaths(getcwd(),'data/'),Null);
        $this->assertEquals($retVal, $checkVal);

    }

    public function testgetAbsolutePathWithDifferentCwd() {

        $retVal = Utils::getAbsolutePath('test.csv',Null,'C:');
        $checkVal = array('C:/data/test.csv',Null);
        $this->assertEquals($retVal, $checkVal);

    }

    public function testgetFileExtensionOfNull() {

        $retVal = Utils::getFileExtension(Null);
        $this->assertEquals($retVal, Null);

    }

    public function testgetFileExtensionOfDirectory() {
     
        $retVal = Utils::getFileExtension("C:/Data");
        $this->assertEquals($retVal, '');

    }

    public function testcreateOutputDirectoryIfNull() {
     
        $retVal = Utils::createOutputDirectory(Null);
        $this->assertEquals($retVal, false);

    }

    private function deleteTestDir() {

        $testDir = Utils::joinPaths(getcwd(),'testdata','testdir');
        Utils::deleteDirectory($testDir);

    }

    public function testcreateOutputDirectoryNewDir() {

        $checkVal = Utils::joinPaths(getcwd(),'testdata','testdir','test.csv');
        $retVal = Utils::createOutputDirectory($checkVal);
        $this->assertEquals($retVal, true);

    }

    public function testcreateOutputDirectoryOfExistingDir() {

        $checkVal = Utils::joinPaths(getcwd(),'testdata','testdir','test.csv');
        $retVal = Utils::createOutputDirectory($checkVal);
        $this->deleteTestDir();
        $this->assertEquals($retVal, false);

    }

    public function testdeleteDirectoryNonExistentDir() {

        $checkVal = Utils::joinPaths(getcwd(),'testdata','testdir');
        $retVal = Utils::deleteDirectory($checkVal);
        $this->assertEquals($retVal, false);

    }

    public function testdeleteDirectoryNull() {

        $retVal = Utils::deleteDirectory(Null);
        $this->assertEquals($retVal, false);

    }
    
}

?>