<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 13:13:27
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 13:13:51
 */
session_start();
$sid = session_id();
if($sid){
    session_destroy();
}

header('location: ');
exit;