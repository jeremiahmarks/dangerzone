<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-02-17 22:40:42
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-27 18:53:48
 */
## I seriously can't believe how much basic information I am 
##  unable to recall.
#If  
if (isset($_POST['video'])){
  insertScript($_POST['video'])
}

SELECT tagapplications.tagid, tags.tagname FROM tagapplications LEFT JOIN tags on tagapplications.tagid = tags.tagid WHERE tagapplications.taskid=1;
SELECT taskProjectAssignments.projectid, taskProjects.projectname FROM taskProjectAssignments LEFT JOIN taskProjects on taskProjectAssignments.projectid = taskProjects.projectid WHERE taskProjectAssignments.taskid=1;

#If/Else
  #From http://www.w3schools.com/php/php_if_else.asp
if (condition) {
    code to be executed if condition is true;
} else {
    code to be executed if condition is false;
}

#If/Elseif/Else
if (condition) {
    code to be executed if condition is true;
} elseif (condition) {
    code to be executed if condition is true;
} else {
    code to be executed if condition is false;
}

#switch
  # From http://www.w3schools.com/php/php_switch.asp
<?php
$favcolor = "red";

switch ($favcolor) {
    case "red":
        echo "Your favorite color is red!";
        break;
    case "blue":
        echo "Your favorite color is blue!";
        break;
    case "green":
        echo "Your favorite color is green!";
        break;
    default:
        echo "Your favorite color is neither red, blue, or green!";
}


#get a list of tables
  #from http://stackoverflow.com/a/4703159/492549
function get_tables()
{
  $tableList = array();
  $res = mysqli_query($this->conn,"SHOW TABLES");
  while($cRow = mysqli_fetch_array($res))
  {
    $tableList[] = $cRow[0];
  }
  return $tableList;
}

  #another potential solution
  #from http://stackoverflow.com/a/4703142/492549
SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA LIKE 'your_database';

#mysql statement to create a new table
$cars = "CREATE TABLE cars(
    carid int(10) NOT NULL auto_increment,
    carowner int(11) NOT NULL,
    make varchar(255),
    model varchar(255),
    plates varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (carid)
    )";

#mysql example of how to store encrypted information
# encryptedInbox is a table with two columns, int(11) id, longblob item
$insertNewIdea = "INSERT into encryptedInbox (item) VALUES (AES_ENCRYPT('Some String', 'myKey'));";
$getTranslation = "SELECT *, AES_DECRYPT(item, 'myKey') FROM encryptedInbox;";

#mysqli_bind_parameters
function addtodo($todotoadd) {
    //This function will be used to add todo items to the proper tables.
    global $conn; //this expects that $conn is defined as 
    // $conn =  mysqli_connect($dbpath, $dbuser,$dbpassword,$dbtouse);
    $stmt = mysqli_stmt_init($conn);
    if (mysqli_stmt_prepare($stmt, "INSERT INTO encryptedInbox (item) VALUES (AES_ENCRYPT(?, ?));"){
      mysqli_stmt_bind_param($stmt, 'ss', $_POST['message'], $key);
      mysqli_stmt_execute($stmt);
      mysqli_stmt_close($stmt);

    }
    $toadd = mysqli_prepare($conn, "INSERT INTO inbox ( item, class) VALUES (?,?)");
    //Above statement
    $class='todo';
    mysqli_stmt_bind_param($toadd, 'ss', $todotoadd, $class);
    mysqli_stmt_execute($toadd);
    $testa = $todotoadd . "todo";
    return $testa;
}
##mysqli_stmt_bind_param parameters
##  3 parameters
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
// Some fun mysql statements

$a='SELECT * FROM catchall, catchalltagapplications WHERE catchall.id = catchalltagapplications.catchallid AND catchall.id = 74';
$searchStmt1='SELECT *
FROM (
    SELECT tagapplications.tagid AS tagid, tags.tagname AS tagname, tasks.taskname AS taskname, tasks.taskid AS tid
    FROM tagapplications
    LEFT JOIN  tags ON tagapplications.tagid = tags.tagid
    LEFT JOIN  tasks ON tagapplications.taskid = tasks.taskid
    WHERE tagapplications.taskid =1
) AS tagside
RIGHT JOIN taskProjectAssignments ON tagside.tid = taskProjectAssignments.taskid
JOIN taskProjects ON taskProjectAssignments.projectid=taskProjects.projectid
WHERE taskProjectAssignments.taskid =1'


$searchStmt2='SELECT *
FROM (
    SELECT tagapplications.tagid AS tagid, tags.tagname AS tagname, tasks.taskname AS taskname, tasks.taskid AS tid
    FROM tagapplications
    LEFT JOIN  tags ON tagapplications.tagid = tags.tagid
    LEFT JOIN  tasks ON tagapplications.taskid = tasks.taskid
    WHERE tagapplications.taskid =1
) AS tagside
RIGHT JOIN taskProjectAssignments ON tagside.tid = taskProjectAssignments.taskid
RIGHT JOIN taskProjects ON taskProjectAssignments.projectid=taskProjects.projectid
WHERE taskProjectAssignments.taskid =1'

$searchStmt3='SELECT *
FROM (
    SELECT tagapplications.tagid AS tagid, tags.tagname AS tagname, tasks.taskname AS taskname, tasks.taskid AS tid
    FROM tagapplications
    LEFT JOIN  tags ON tagapplications.tagid = tags.tagid
    LEFT JOIN  tasks ON tagapplications.taskid = tasks.taskid
    WHERE tagapplications.taskid =1
) AS tagside
LEFT JOIN taskProjectAssignments ON tagside.tid = taskProjectAssignments.taskid
LEFT JOIN taskProjects ON taskProjectAssignments.projectid=taskProjects.projectid
WHERE taskProjectAssignments.taskid =1'

$searchStmt4='SELECT tagside.tagid AS tagid, tagside.tagname as tagname, tagside.taskname as taskname, tagside.tid as tid, taskProjectAssignments.projectid as pid, taskProjects.projectname as pname, taskProjects.projectDescription as descp
FROM (
    SELECT tagapplications.tagid AS tagid, tags.tagname AS tagname, tasks.taskname AS taskname, tasks.taskid AS tid
    FROM tagapplications
    LEFT JOIN  tags ON tagapplications.tagid = tags.tagid
    LEFT JOIN  tasks ON tagapplications.taskid = tasks.taskid
    WHERE tagapplications.taskid =1
) AS tagside
LEFT JOIN taskProjectAssignments ON tagside.tid = taskProjectAssignments.taskid
LEFT JOIN taskProjects ON taskProjectAssignments.projectid=taskProjects.projectid
WHERE taskProjectAssignments.taskid =1'