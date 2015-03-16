<?php
session_start();
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-02-16 17:58:39
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-03-15 01:15:28
 */

/**
* This will start as a collection of functions from prior php projects.
**/

  include_once'connection.php';

  function pp($arr){ /*pretty print*/
    //Provides a pretty way to see what an array contains. 
    //Also is a recursive function.  
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

  function getall($tablename, $conn){/*gets all of the results from $tablename */
    $query = "SELECT * FROM {$tablename}";
    echo $query;
    $results = mysqli_query( $conn , $query );
    return $results;
    // if($results = mysqli_query( $conn , $query )){
    //   return $results;
    // }
  }

  function thisTest($conn, $tablename){
    $res=getall($tablename, $conn);
    echo pp($re);
  }
?>