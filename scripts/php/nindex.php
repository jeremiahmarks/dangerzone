<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-02-16 18:23:58
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-02-16 19:41:04
 */
# This is starting as a direct copy of what I have at portfolio.jlmarks.org
session_start();
  include "header.php";
  include_once 'functions.php';
  include_once 'connection.php';
  include "my.pw.php";

  if (isset($_POST['login'])){ 
  /* if the user attempts to sign in, ensure that
  the username and password are this and then 
  set the islogged session variable to 1
  */
    if (($_POST['username']=='jlmarks') 
        && 
        ($_POST['password']=='jlmarks')){
      $_SESSION['islogged']=1;
    }
  }

    if(isset($_POST['logout'])){
        unset($_SESSION['islogged']);
    }

  if(isset($_SESSION['islogged'])){ ?>
<form action='' method='post'>
    <input type='submit' name='logout' value='logout' />
</form>


<?php
                                  }
  
  if (isset($_POST['newcode'])){
    addcode($conn, $_POST);
  }
  
  if (isset($_POST['deletecode'])){
      deletecode($conn, $_POST);
  }

  if (isset($_POST['onlythis']) and ($_POST['onlythis']!='All') ){
      $_SESSION['specific']=$_POST['onlythis'];
  } elseif ($_POST['onlythis']=='All'){
      unset($_SESSION['specific']);
  }



 $projects=getinfo($conn,"portfolio");


  echo "<div class='projectholder'>";
  while($row=mysqli_fetch_array($projects)){
    ?> 
    <div id="<?php echo  $row['id']; ?>" class=" hide project <?php echo $row['language']; ?>">
    <?php if(isset($_SESSION['islogged'])){ 
    ?>
        <form action='' method='post'><input name='deletecode' value = '<?php echo $row["id"]; ?>' type='submit'></form>
       
        <?php } ?>
      <image class = "projectimage" src="<?php echo $row['piclocation']; ?>" />
      <h1><a href="<?php echo $row['sourcecode']; ?>"><?php echo $row['name']; ?></a></h1>
      <div class="dateadded"><?php echo $row['dateadded']; ?></div>
      <div class="aboutproject">

      <p><?php echo $row['about']; ?></p>
    </div>
    </div>
    <?php 
  }  echo "</div>";

  if (!isset($_SESSION['islogged'])){?>
  
<div id="myfooter"> 
  <form action='' method='post'>
    <input type='text' name='username'>
    <input type='password' name='password'>
    <input type='submit' name='login' value='login'>
  <form>

</div>
  <?php } 
  else {
    addproject();
  }

include 'footer.php';
?>
