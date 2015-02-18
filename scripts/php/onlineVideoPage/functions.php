<?php
require 'config.php';
/**
 * @Author: jeremiah.marks
 * @Date:   2015-02-17 14:23:45
 * @Last Modified by:   jeremiah.marks
 * @Last Modified time: 2015-02-17 14:48:31
 */
$conn =  mysqli_connect($dbpath, $dbuser,$dbpassword,$dbtouse);
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}
function pp($arr){ /*pretty print*/
    $retStr = '<ul>';
    if (is_array($arr)){
        foreach ($arr as $key=>$val){
            if (is_array($val)){
                $retStr .= '<li>' . $key . ' => ' . pp($val) . '</li>';
            }else{
                $retStr .= '<li>' . $key . ' => ' . $val . '</li>';
            }
        }
    }
    $retStr .= '</ul>';
    return $retStr;
}

function nspp($arr){
  $retStr = '[';
  if (is_array($arr)){
    foreach ($arr as $key=>$val){
      if (is_array($val)){
        $retStr .= '[' . $key . ':' . nspp($val) . ']';
      } else {
        $retStr .= '[' . $key . ':' . $val . ']';
      }
    }
  }
  $retStr .= ']';
  return $retStr;
}

function addtodo($todotoadd) {
    //This function will be used to add todo items to the proper tables.
    global $conn;
    $toadd = mysqli_prepare($conn, "INSERT INTO inbox ( item, class) VALUES (?,?)");
    $class='todo';
    mysqli_stmt_bind_param($toadd, 'ss', $todotoadd, $class);
    mysqli_stmt_execute($toadd);
    $testa = $todotoadd . "todo";
    return $testa;
}