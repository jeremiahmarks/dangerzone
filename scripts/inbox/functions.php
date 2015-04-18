<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 22:20:21
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-18 12:21:30
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
## catchalltagapplications
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


function addTagToContactRecord($catchallid, $catchalltagid){
    global $conn;
    $checkString = 'SELECT COUNT(*) FROM catchalltagapplications WHERE catchallid=' . $catchallid . ' AND catchalltagid=' . $catchalltagid ;
    $results=mysqli_query($conn, $checkString);
    $numOfMatches=mysqli_fetch_array($results);
    if ( $numOfMatches[0]==0 ){
        $stmtString = "INSERT INTO catchalltagapplications (catchallid, catchalltagid) VALUES (?,?)";
        $stmt = mysqli_prepare($conn, $stmtString);
        mysqli_stmt_bind_param($stmt, 'ii', $catchallid, $catchalltagid);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
    }
}

function add_item($itemName){
    global $conn;
    // echo $_POST['newItem'];
    if (isset($_POST["notes"])){
        $stmtString = "INSERT INTO catchall (text,notes) VALUES (?,?)";
        $stmt = mysqli_prepare($conn, $stmtString);
        mysqli_stmt_bind_param($stmt, 'ss', $itemName, $_POST["notes"]);
    } else {
        $stmtString = "INSERT INTO catchall (text) VALUES (?)";
        $stmt = mysqli_prepare($conn, $stmtString);
        mysqli_stmt_bind_param($stmt, 's', $itemName);
    }
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    $thisnotesID=mysqli_insert_id($conn);
    if (isset($_POST['tags'])){
        foreach ($_POST['tags'] as $key => $value) {
            addTagToContactRecord($thisnotesID, $value);
        }
    }
}

function convert_data_to_HTMLoption($dataSet){
    //currently expecting that the key will be an integer
    $sbuilder="<div class=\"tagOptions\">\n
    <select name=\"tags[]\" class=\"tagList\" multiple>";
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

function get_all_tagapplications(){
    global $conn;
    $getAllStmt = "SELECT id, catchallid, catchalltagid FROM catchalltagapplications";
    $applicationData=array();
    $applicationResults=mysqli_query($conn, $getAllStmt);
    while ($eachRow = mysqli_fetch_array($applicationResults)){
        $applicationData[$eachRow['id']]=array( "catchallid" => $eachRow['catchallid'], "catchalltagid" => $eachRow['catchalltagid']);
    }
    return $applicationData;
}

function get_all_catchalls_with_tag($catchalltagid){
    global $conn;
    $getAllStmt = "SELECT id, catchallid, catchalltagid FROM catchalltagapplications WHERE catchalltagid = ? ";
    $applicationData=array();
    if ($stmt = mysqli_prepare($conn, $getAllStmt)){
        mysqli_stmt_bind_param($stmt, 'i', $catchalltagid);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_bind_result($stmt, $id, $catchallid, $catchalltagid);
        while (mysqli_stmt_fetch($stmt)){
            $applicationData[$id] = array($catchallid, $catchalltagid);
        }
        mysqli_stmt_close($stmt);
    }
    return $applicationData;
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

function get_catchall_all($catchallid){
    global $conn;
    $catchallAll=array();
    $get_txt_stmt = "SELECT text, created FROM catchall WHERE id = ?";
    if ($stmt = mysqli_prepare($conn, $get_txt_stmt)){
        mysqli_stmt_bind_param($stmt, 'i', $catchallid);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_bind_result($stmt, $text, $created);
        while (mysqli_stmt_fetch($stmt)){
            $catchallAll['catchallid'] = $catchallid;
            $catchallAll['text']=$text;
            $catchallAll['created']=$created;
        }
        mysqli_stmt_close($stmt);
    }
    return $catchallAll;
}

function get_tags_applied($catchallid){
    global $conn;
    $stmtString = "SELECT id, catchalltagid, applied FROM catchalltagapplications WHERE catchallid = ?";
    $allTagsAppliedData=array();
    if ($stmt = mysqli_prepare($conn, $stmtString)){
        mysqli_stmt_bind_param($stmt, 'i', $catchallid);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_bind_result($stmt, $id, $catchalltagid, $applied);
        while (mysqli_stmt_fetch($stmt)){
            $allTagsAppliedData[$id] = array( 'catchalltagid' => $catchalltagid, 'applied' => $applied);
        }
        mysqli_stmt_close($stmt);
    }
    return $allTagsAppliedData;
}

function get_tags_as_option(){
    $tagsData = get_all_tags();
    return convert_data_to_HTMLoption($tagsData);


}

function main_page(){
    htmlHead();
    bodyStart();
    inboxSubmitter();
    listAllNotes();
    footer();
    print_r($_POST);
    if (isset($_POST['tags'])){
        print_r($_POST['tags']);
        foreach ($_POST['tags'] as $value) {
            // echo $key;
            echo $value;
            echo "\n\n";
        }
    }
    bodyEnd();
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

function update_catchall_text($catchallid, $catchalltext){
    global $conn;
    $stmtString = "UPDATE catchall SET text = ? WHERE id = ? ";
    $stmt = mysqli_prepare($conn, $stmtString);
    print_r($stmt);
    mysqli_stmt_bind_param($stmt, 'si',  $catchalltext, $catchallid );
    mysqli_stmt_execute($stmt);
    print_r($stmt);
    mysqli_stmt_close($stmt);
    // return $callresults;
}
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