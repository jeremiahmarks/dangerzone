<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 22:21:51
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-14 23:35:33
 */

include_once "functions.php";
##will enable access to 

## add_item(itemName);
## main_page()

function brain(){
    global $conn;
    if (isset($_POST['newItem'])){
        add_item($_POST['noteText']);
        main_page();
    } elseif (isset($_POST['newTag'])){
        
        echo new_tag($_POST['newTagName'], $_POST["tagDescription"]);
        main_page();
    } elseif (isset($_POST['updateRecord'])) {
        $catchallid=$_POST['catchallid'];
        print_r($catchallid);
        if ( isset($_POST['catchallText'] )){
            echo update_catchall_text($catchallid, $_POST['catchallText']);
            editItem(array('id' => $catchallid ));
        }
        
    } else {
        main_page();
    }
}