<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 03:42:36
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 03:48:52
 */
$pwpath = $_SERVER['DOCUMENT_ROOT'] . "/tasks/my.pw.php";
include_once($pwpath);
$conn =  mysqli_connect($iinbox_db_address, $iinbox_username ,$iinbox_password,$iinbox_db_name);
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}