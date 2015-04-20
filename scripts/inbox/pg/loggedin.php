<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 16:38:16
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 23:20:25
 */
function loggedinIncluded(){}
include_once 'htmlLoggedinElements.php';
$htmlFactory = new loggedHtmlBuilder();
$htmlFactory->generate_logged_in_page();