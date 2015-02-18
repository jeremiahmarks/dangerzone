<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-02-17 22:40:42
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-02-17 23:47:30
 */
## I seriously can't believe how much basic information I am 
##  unable to recall.
#If  
if (isset($_POST['video'])){
  insertScript($_POST['video'])
}

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