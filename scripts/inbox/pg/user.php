<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 03:31:47
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 15:11:57
 */
session_start();

include_once 'dbmagic.php';

class userRecord{
    private $data = array();

    public function __construct(){}

    public static function factory()
    {
        if (isset($_SESSION['user']))
        {
            return unserialize($_SESSION['user']);
        }
        return new userRecord();
    }

    public function __set($property, $value)
    {
        $this->data[$property] = $value;
    }

    public function __get($property)
    {
        if ( isset( $this->data[$property] ) )
        {
            return $this->data[$property];
        }
    }

    public function __destruct()
    {
        $_SESSION['user'] = serialize($this);
    }
}


if (isset($_GET['logout'])){
    include_once 'logout.php';
} else {
    if (isset($_SESSION['loggedIn'])){
        if ($_SESSION['loggedIn']==1){
            include_once 'loggedin.php';
        } else {
            include_once 'unknownuser.php';
        }
    } else {
        $_SESSION['loggedin'] = 0;
        include_once 'unknownuser.php';
    }
}