<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-14 13:15:55
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-14 14:01:35
 */

session_start();

include_once 'connection.php';

if isset($_POST['logout']){
    session_unset();
    session_destroy();
}
if isset($_POST['newUser']){
    $checkString = 'SELECT COUNT(*) FROM catchallusers WHERE username=' . $_POST['username'];
    $results=mysqli_query($conn, $checkString);
    $numOfMatches=mysqli_fetch_array($results);
    if ( $numOfMatches[0]==0 ){
        $username = $_POST['username'];
        $password = $_POST['password'];

        $cost = 10; 
        $salt = strtr(base64_encode(mcrypt_create_iv(16, MCRYPT_DEV_URANDOM)), '+', '.');
        $salt = sprintf("$2a$%02d$", $cost) . $salt;
        $hash = crypt($password, $salt);
        $stmtString = "INSERT INTO catchallusers (username, password) VALUES (?,?)";
        $stmt = mysqli_prepare($conn, $stmtString);
        mysqli_stmt_bind_param($stmt, 'ss', $username, $hash);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
        $_SESSION['userid'] = mysqli_insert_id($conn);
    }
}
}
if isset($_POST['login']){

}