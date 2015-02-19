<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-02-18 21:49:28
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-02-18 23:54:42
 */
include_once 'functions.php';
global $conn;
echo "something, hopefully!";
if (isset($_POST['mode'])){
  echo "mode is set";
  switch ($_POST['mode']) {
    case 'save':
      # code
      # make sure that there is also a dataset and 
      # an encryption key
    echo "case: save";
    if(isset($_POST['message'])){
      if(!isset($_POST['key'])){
        $key = '';
      } else{
        $key=$_POST['key'];
      }

      //This function will be used to add todo items to the proper tables.
       //this expects that $conn is defined as 
      // $conn =  mysqli_connect($dbpath, $dbuser,$dbpassword,$dbtouse);
      $stmt = mysqli_stmt_init($conn);
      if  ( mysqli_stmt_prepare($stmt, "INSERT INTO encryptedInbox (item) VALUES (AES_ENCRYPT(?, ?));") ){
        echo "red";
        mysqli_stmt_bind_param($stmt, 'ss', $_POST['message'], $key);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
      }
      }
      break;
    
    default:
      echo "default";
      break;
  }
} else {
  ?>
  <html>
    <form action="" method="post">
      Message: <input type="text" name='message'><br />
      key: <input type="text" name='key' /><br />
      <input type="submit" name="mode" value="save" />
    </form>
  </html>
<?php
}