<?php



$pwpath = $_SERVER['DOCUMENT_ROOT'] . "/tasks/my.pw.php";
include_once($pwpath);
$conn =  mysqli_connect($mysql_db_address, $mysql_username ,$mysql_password,$mysql_db_name);
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}
