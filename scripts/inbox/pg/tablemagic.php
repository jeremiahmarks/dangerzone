<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 12:17:39
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 18:28:42
 */

////////////////////////////////////////////////////////////
//  I am really happy I highly commented this the last time
//  I did it: https://github.com/jeremiahmarks/valet/blob/master/createvaletdb.php

// $dropping=mysql_query("DROP TABLE IF EXISTS customers");
// CREATE TABLE tablename (field1name field1datatype field1modifiers, field2name field2datatype field2modifiers ... PRIMARY KEY (primarykeyname))
// $customers = "CREATE TABLE customers (
//   customer_id int(11) NOT NULL auto_increment,
//   fname varchar(255),
//   lname varchar(255) NOT NULL,
//   phone varchar(15) NOT NULL,
//   email varchar(255) NOT NULL UNIQUE,
//   address1 text,
//   address2 text,
//   city text,
//   state text,
//   zip text,
//   emer_name varchar(255),
//   emer_num varchar(255),
//   PRIMARY KEY(customer_id)
//   )";
//  CREATE TABLE `database`.`tablename` (
// `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
// `updated` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL ,
// `pwdata` BLOB NOT NULL COMMENT 'pwdata'
// ) 

include_once 'connection.php';
global $conn;

function create_table($tablename, $tablecriteria){
    global $conn;
    $queryStmt = "CREATE TABLE " . $tablename . " ( " . $tablecriteria . " ) ENGINE=INNODB;";//need engine statement
    $stmt = mysqli_stmt_init($conn);
    echo $queryStmt;
    if (mysqli_stmt_prepare($stmt, $queryStmt)){
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
    }
}
function drop_table($tablename){
    global $conn;
    $queryStmt="DROP TABLE IF EXISTS " . $tablename;
    $stmt = mysqli_prepare($conn, $queryStmt);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
}
function iinboxusers_criteria(){
    return "
    id int(11) NOT NULL auto_increment,
    fname varchar(255),
    lname varchar(255),
    email varchar(255) NOT NULL UNIQUE,
    pwdata BLOB NOT NULL,
    verified bool NOT NULL default 0,
    admin bool NOT NULL default 0,
    PRIMARY KEY(id)";
}

function iinboxitems_criteria(){
    return "
    id int(11) NOT NULL auto_increment,
    ownerid int(11) NOT NULL,
    title varchar(255),
    notes text NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    KEY ownerid (ownerid, title),
    FOREIGN_KEY (ownerid) REFERENCES iinboxusers(id)
    ";
}

function iinboxtags_criteria(){
    return "
    id int(11) NOT NULL auto_increment,
    ownerid int(11) NOT NULL,
    title varchar(255),
    notes text NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    KEY ownerid (ownerid, title),
    FOREIGN_KEY (ownerid) REFERENCES iinboxusers(id)
    ";
}
function iinboxtagapplication_criteria(){
    return "
    id int(11) NOT NULL auto_increment,
    ownerid int(11) NOT NULL,
    iinboxitemsid int(11) NOT NULL,
    iinboxtagsid int(11) NOT NULL,
    KEY ownerid (ownerid, title),
    FOREIGN_KEY (ownerid) REFERENCES iinboxusers(id),
    FOREIGN_KEY (iinboxitemsid) REFERENCES iinboxitems(id),
    FOREIGN_KEY (iinboxtagsid) REFERENCES iinboxtags(id)";
}
function createUsers(){
    $tname="iinboxusers";
    $tcrit=iinboxusers_criteria();
    drop_table($tname);
    create_table($tname, $tcrit);
}
function createItems(){
    $tname = "iinboxitems";
    $tcrit = iinboxitems_criteria();
    drop_table($tname);
    create_table($tname, $tcrit);
}

function createTags(){
    $tname = "iinboxtags";
    $tcrit = iinboxtags_criteria();
    drop_table($tname);
    create_table($tname, $tcrit);
}
function createTagApplications(){
    $tname = 'iinboxtagapplications';
    $tcrit = iinboxtagapplication_criteria();
    drop_table($tname);
    create_table($tname, $tcrit);
}

createUsers();
createItems();
createTags();
createTagApplications();