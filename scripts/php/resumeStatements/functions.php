<?php
session_start();
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-03-15 00:55:43
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-03-15 16:42:54
 */

include_once'connection.php';
include 'htmlElements.php';

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

function getall($tablename){/*gets all of the results from $tablename */
    global $conn;
    $query = "SELECT * FROM {$tablename}";
    $dataList= array();
    $results = mysqli_query( $conn , $query );
    while ($eachRow = mysqli_fetch_array($results))
    {
      $dataList[] = $eachRow;
    }
    return $dataList;
// if($results = mysqli_query( $conn , $query )){
//   return $results;
// }
}

function getStatements(){
    global $conn;
    $statementsquery = "SELECT id, statement from resStmts";
    $tagsQuery="SELECT id, tagname from restags";
    $tagAppliedQuery = "SELECT applicationid, resstatementid, restagid FROM restagsapplied";
    $_SESSION['statements'] = array();
    $_SESSION['tags']=array();
    $_SESSION['applications']=array();
    $_SESSION['tagsToStmts'] = array();
    $_SESSION['stmtsToTags'] = array();
    $stmtResults = mysqli_query( $conn, $statementsquery );
    while ($eachRow = mysqli_fetch_array($stmtResults)){
        $_SESSION['statements'][$eachRow['id']] = $eachRow['statement'];
        $_SESSION['stmtsToTags'][$eachRow['id']]=array();
    }
    $tagsResults = mysqli_query($conn, $tagsQuery);
    while ($eachRow = mysqli_fetch_array($tagsResults)){
        $_SESSION['tags'][$eachRow['id']] = $eachRow['tagname'];
        $_SESSION['tagsToStmts'][$eachRow['id']] = array();
    }
    $applicationResults = mysqli_query($conn, $tagAppliedQuery);
    while ($eachRow = mysqli_fetch_array($applicationResults)){
        $_SESSION['applications'][$eachRow['applicationid']] = [ "stmtid" => $eachRow['resstatementid'], "tagid" => $eachRow['restagid'] ];
        $_SESSION['stmtsToTags'][$eachRow['resstatementid']][]=$eachRow['restagid'];
        $_SESSION['tagsToStmts'][$eachRow['restagid']][]=$eachRow['resstatementid'];
    }
}
function printAllLines(){
    getStatements();
    echo "<h1>Statements</h1>";
    echo pp($_SESSION['statements']);
    echo "<h1>Tags</h1>";
    echo pp($_SESSION['tags']);
    echo "<h1>Applications</h1>";
    echo pp($_SESSION['applications']);
    echo "<h1>Tags to Statements</h1>";
    echo pp($_SESSION['tagsToStmts']);
    echo "<h1>Statements to Tags</h1>";
    echo pp($_SESSION['stmtsToTags']);
}

function printStmtsWithTags(){
    headerStart();
    bodyStart();
    getStatements();
    foreach ($_SESSION['statements'] as $key => $value) {
        addStatementWithTags($key);
    }
    bodyEnd();
}

function applyTagToStmt($statementid, $tagid){
    global $conn;
    $checkStmt='SELECT COUNT(1) FROM restagsapplied WHERE resstatementid=' . $statementid . ' AND restagid=' . $tagid ;
    $results=mysqli_query($conn, $checkStmt);
    $numOfMatches=mysqli_fetch_array($results);
    if ( $numOfMatches[0]==0 ){
        $addStmt = mysqli_prepare($conn, "INSERT INTO restagsapplied (resstatementid, restagid) VALUES (?,?)");
        mysqli_stmt_bind_param($addStmt, 'ii', $statementid, $tagid);
        mysqli_stmt_execute($addStmt);
    } else{
        echo "Could not apply!";
    }
}

function removeTag($statementid, $tagid){
    global $conn;
    $rmStmt = 'DELETE FROM restagsapplied WHERE resstatementid=' . $statementid . ' AND restagid=' . $tagid ;
    mysqli_query($conn, $rmStmt);
}

function infoParser(){
    if (isset($_POST['tagAdd']) || isset($_POST['tagRemove'])){
        // return pp($_POST);
        if (isset($_POST['tagAdd'])){
            foreach ($_POST['tagAdd'] as $key => $value) {
                applyTagToStmt($_POST['statementID'], $value);
            }
        }
        if (isset($_POST['tagRemove'])){
            foreach ($_POST['tagRemove'] as $key => $value) {
                removeTag($_POST['statementID'], $value);
            }
        }
        getStatements();
        return interiorInfo($_POST['statementID']);
    } elseif (isset($_POST['statementID'])) {
        return pp($_POST);
        // return "I SEE A statementid!";
    }else{
        printStmtsWithTags();
    }
}