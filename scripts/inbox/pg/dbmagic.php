<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 12:15:43
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 23:08:44
 */
session_start();
require_once ('connection.php');
global $conn;
$pwpath = $_SERVER['DOCUMENT_ROOT'] . "/phppw/password.php";
require $pwpath;

class dbcalls{
    private $dbconn;
    private $error_feedback=array();
    public function __construct(){}
    private function check_data_user_create(){
        if (!isset($_POST['username']))
        {
            $this->error_feedback[] = 'missing email information';
        } else {
            $otherUsers = $this->get_count_of_instances_in_iinboxusers($_POST['username']);
            if (!($otherUsers == 0)){
                $this->error_feedback[] = 'this username exists';
            }
        }
        if (!isset($_POST['password']))
        {
            $this->error_feedback[] = 'missing password information';
        }
        return (empty($this->error_feedback));
    }
    public function get_count_of_instances_in_table($table, $cols, $value){
        if (is_string($cols)){
            $iqueryStmt = "SELECT COUNT(1) FROM ? WHERE ? = ?";
            $istmt = mysqli_prepare($this->dbconn, $iqueryStmt);
            mysqli_stmt_bind_param($istmt, 'sss', $table, $cols, $value);
            mysqli_stmt_execute($istmt);
            mysqli_stmt_bind_result($istmt, $callResult);
            while (mysqli_stmt_fetch($istmt)) {
                $totalInstances=$callResult;
            }
            mysqli_stmt_close($istmt);
            return $totalInstances;
        }
    }
    public function get_count_of_instances_in_iinboxusers($email){
        $queryStmt = "SELECT COUNT(1) FROM iinboxusers WHERE email = ?";
        $stmt = mysqli_prepare($this->dbconn, $queryStmt);
        mysqli_stmt_bind_param($stmt, 's', $email);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_bind_result($stmt, $results);
        while (mysqli_stmt_fetch($stmt)){
            $actualcount = $results;
        }
        mysqli_stmt_close($stmt);
        echo "\nactualcount = " . $actualcount . "\n\n";
        return $actualcount;
    }
    public function set_connection($connection){
        $this->dbconn = $connection;
    }
    public function user_create(){
        global $conn;
        if ($this->check_data_user_create()){
            $username = $_POST['username'];
            $password = $_POST['password'];
            // $cost = 10; 
            // $salt = strtr(base64_encode(mcrypt_create_iv(16, MCRYPT_DEV_URANDOM)), '+', '.');
            // $salt = sprintf("$2a$%02d$", $cost) . $salt;
            $hash = password_hash($password, PASSWORD_BCRYPT);
            $stmtString = "INSERT INTO iinboxusers (email, pwdata) VALUES (?,?)";
            $stmt = mysqli_prepare($this->dbconn, $stmtString);
            mysqli_stmt_bind_param($stmt, 'ss', $username, $hash);
            mysqli_stmt_execute($stmt);
            mysqli_stmt_close($stmt);
            $_SESSION['userid'] = mysqli_insert_id($conn);
        } else {
            if (!empty($this->error_feedback)){
                foreach ($this->error_feedback as $key => $value) {
                    echo "\nerror_feedback\n" . $value . "\n\n";
                }
            } else {
                echo "Unknown Issue";
                print_r($conn);
            }
        }
    }
    public function user_credential_verification($username, $password){
        global $conn;
        $queryStmt = "SELECT id, pwdata FROM iinboxusers WHERE email = ? LIMIT 1";
        $stmt = mysqli_prepare($conn, $queryStmt);
        mysqli_stmt_bind_param($stmt, 's', $username);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_bind_result($stmt, $userid, $callResult);
        while (mysqli_stmt_fetch($stmt)) {
            $storedHash=$callResult;
            $hashesID=$userid;
        }
        mysqli_stmt_close($stmt);
        if (password_verify($password, $storedHash)){
            $_SESSION['uid'] = $hashesID;
            return true;
        }
    }
}