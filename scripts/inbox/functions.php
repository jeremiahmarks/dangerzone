<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 22:20:21
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-10 23:23:22
 */
##
include_once 'connection.php';
include_once 'htmlElements.php';
########
########
##Current List of functions:
##
## add_item(itemName);
## main_page()
## get_all_notes()


########
########
## Current lists of tables to access through $conn:
##
## catchall
## id - integer ID
## text - text of submission
## datetime - datetime created
##
## catchalltags
## id - integer ID
## displayText - varchar(32)
## notes - varchar(256)
## 
## catchalltagapplied
## id - unique id for this particular application
## catchallid - id of catchall
## catchalltagid - id of the tag





function add_item($itemName){
    global $conn;
    $error='';
    $stmtString = "INSERT INTO catchall (text) VALUES (?)";
    $stmt = mysqli_prepare($conn, $stmtString);
    mysqli_stmt_bind_param($stmt, 's', $itemName);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
}

function main_page(){
    htmlHead();
    bodyStart();
    inboxSubmitter();
    // listAllNotes();
    footer();
    bodyEnd();
}

function get_all_notes(){
    global $conn;
    $notesStmt = "SELECT * FROM catchall";
    $notesData=array();
    $notesResults=mysqli_query($conn, $notesStmt);
    while ($eachRow = mysqli_fetch_array($notesResults)){
        $notesData[$eachRow['id']]=$eachRow['text'];
    }
    return $notesData;
}
