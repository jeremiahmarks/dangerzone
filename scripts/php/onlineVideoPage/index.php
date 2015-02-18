<?php
session_start();
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-02-16 23:17:05
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-02-18 00:46:05
 */

/**
* First things fist: ensure that I can access a variable
*   passed through the url
*/
include_once 'functions.php';
include_once 'my.pw.php';
include 'head.php';
if (isset($_POST['add'])){
  add_video_to_database($_POST['add']);
}
elseif (isset($_POST['video'])){
  insertScript($_POST['video']);
} else {
  insertScript("UpdateBillingInfo");
}
include 'body.php';

?>