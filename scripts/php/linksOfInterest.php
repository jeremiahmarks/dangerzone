<?php
/**
 * @Author: jlmarks
 * @Date:   2015-02-16 17:27:26
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-02-16 18:03:48
 * 
 * Purpose:
 *		This file will store links that I find useful in a database where I can attach tags to them
 *		It will autogenerate a list of pages with all tags, by default, and offer to sort by tags
 *		It will allow someone to submit links without logging in, however it will only display links
 *		which have at least one tag. 
 *		It will a loggedIn tag that will stop those links from being displayed on a public page.
 *
 */

/**
* include a password file to log into the sql server
*
*/
include 'functions.php'

$this_test = 