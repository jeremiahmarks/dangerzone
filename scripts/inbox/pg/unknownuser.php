<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 13:23:30
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 16:16:02
 */
session_start();
include_once 'connection.php';
global $conn;
include_once 'dbmagic.php';
$dbm = new dbcalls();
$dbm->set_connection($conn);
if (isset($_POST['createUser'])) {
    $dbm->user_create();
    include_once 'loginform.php';
}
if (isset($_GET['n'])){
    include_once 'newuserform.php';
}
if (isset($_GET['l'])){
    include_once 'loginform.php';
}
if (isset($_POST['login'])){
    $username = $_POST['username'];
    $password = $_POST['password'];
    if ( $dbm->user_credential_verification($username, $password) ){
        $_SESSION['loggedIn']=1;
        include_once 'loggedin.php';
    } else {
        include_once 'newuserform.php';
    }
}