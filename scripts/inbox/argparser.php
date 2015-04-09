<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 22:21:51
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-08 23:41:15
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
    } else {
        main_page();
    }
}