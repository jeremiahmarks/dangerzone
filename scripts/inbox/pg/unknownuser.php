<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 13:23:30
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 21:44:44
 */
session_start();
include_once 'connection.php';
global $conn;
include_once 'dbmagic.php';

$dbm = new dbcalls();
$dbm->set_connection($conn);

if (isset($_POST['createUser'])) {
    $dbm->user_create();
}


if (isset($_POST['login'])){
    $username = $_POST['username'];
    $password = $_POST['password'];
    if ( $dbm->user_credential_verification($username, $password) ){
        $_SESSION['loggedIn']=1;
        include_once 'loggedin.php';
    } 
}

if (function_exists(loggedinIncluded)){

} else {
    include 'htmlNewuserform.php';
    include 'htmlLoginform.php';
    include 'htmlUnloggedElements.php';
    include_once 'htmlHeader.php';
    unlogged_nav();
    loginForm();
    newUserForm();
}