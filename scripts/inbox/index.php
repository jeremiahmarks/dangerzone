<?php
session_start();
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 22:15:29
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-08 23:43:00
 */

##First lets get a connection to the database
include_once "connection.php";

##Now lets bring in our commonly used functions:
include_once "functions.php";

###This is the main logic unit of the site
include_once "argparser.php";

##Let the brain from argparser do its thing
brain();