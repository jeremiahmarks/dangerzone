<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 22:21:51
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 03:16:20
 */

include_once "functions.php";
##will enable access to 

## add_item(itemName);
## main_page()

function brain(){
    global $conn;
    if (isset($_POST['newItem']))
    {
        add_item($_POST['noteText']);
        main_page();
    } 
    elseif (isset($_POST['newTag']))
    {
        echo new_tag($_POST['newTagName'], $_POST["tagDescription"]);
        main_page();
    } 
    elseif (isset($_POST['editCatchallSubmit'])) {
        process_catchall_update();
        main_page();
    }
    elseif (isset($_POST['updateRecord'])) 
    {
        $catchallid=$_POST['catchallid'];
        print_r($catchallid);
        if ( isset($_POST['catchallText'] ))
        {
            echo update_catchall_text($catchallid, $_POST['catchallText']);
            editItem(array('id' => $catchallid ));
            include_once 'test.php';
        }
        
    } 
    elseif (isset($_GET['preset']))
    {
        presets($_GET['preset']);
        main_page();
    }
    elseif (isset($_GET['test'])) 
    {
        include_once 'test.php';
        # code...
    } 
    // elseif (isset($_GET['editCatchall'])) 
    // {
    //     include_once 'editCatchall.php';
    //     # code...
    // } 
    else 
    {
        main_page();
    }
}