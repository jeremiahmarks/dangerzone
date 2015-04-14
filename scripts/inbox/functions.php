<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 22:20:21
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-13 20:34:34
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


###############
###############
## bind param things I always forget
## mysqli_stmt_bind_param(mysqli_stmt $stmt , string $types , mixed &$var1 [, mixed &$... ])
  ## 1. mysqli_stmt $stmt - this is the statment that you have prepared.
  ## 2. string $types - this lets the function know how to intrpet the data you are about to give item
  ## 3. mixed &$var1 [, mixed &$... ]) - This is the information that you are passing it.  A note:  the 
      ## #number of question marks in step 1 should equal the number of chars in step two
      ## #should equal the number of objects you are passing it in step 3

## format of the second parameter
// i corresponding variable has type integer
// d corresponding variable has type double
// s corresponding variable has type string
// b corresponding variable is a blob and will be sent in packets


function add_item($itemName){
    global $conn;
    $error='';
    echo $_POST['newItem'];
    $stmtString = "INSERT INTO catchall (text) VALUES (?)";
    $stmt = mysqli_prepare($conn, $stmtString);
    mysqli_stmt_bind_param($stmt, 's', $itemName);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
}

function new_tag($displayText, $notes){
    global $conn;
    echo "I am here!";
    $stmtString = "INSERT INTO catchalltags (displayText, notes) VALUES (?,?)";
    $stmt = mysqli_prepare($conn, $stmtString);
    mysqli_stmt_bind_param($stmt, 'ss', $displayText, $notes);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    return mysqli_insert_id($conn);
}

function main_page(){
    htmlHead();
    bodyStart();
    inboxSubmitter();
    listAllNotes();
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

function get_all_tags(){
    global $conn;
    $tagsStmt = "SELECT * FROM catchalltags";
    $tagsData=array();
    $tagsResults=mysqli_query($conn, $tagsStmt);
    while ($eachRow = mysqli_fetch_array($tagsResults)){
        $tagsData[$eachRow['id']]=$eachRow['displayText'];
    }
    return $tagsData;
}

function convert_data_to_HTMLoption($dataSet){
    //currently expecting that the key will be an integer
    $sbuilder="<div class=\"tagOptions\">\n
    <select name=\"tags\" class=\"tagList\" multiple>";
    foreach ($dataSet as $key => $value) {
            $colorID = ($key%2==0 ? "even" : "odd");
            $sbuilder .= "
            <option class=\"noteHolder " . $colorID . "\" value=\"" . $key . "\">" . $value . "</option>
            ";
    }
    $sbuilder .= "</select>
    </div>
    ";
    return $sbuilder;
}

function get_tags_as_option(){
    $tagsData = get_all_tags();
    return convert_data_to_HTMLoption($tagsData);


}

