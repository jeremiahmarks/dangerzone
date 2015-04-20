<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-14 15:41:55
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-14 16:52:41
 */

include_once 'htmlElements.php';
$params=array( "id" => 35);
htmlHead();
bodyStart();
editItem($params);
footer();
bodyEnd();