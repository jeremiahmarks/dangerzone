<?php

 include_once'connection.php';


  
  function pp($arr){ /*pretty print*/
      $retStr = '<ul>';
      if (is_array($arr)){
          foreach ($arr as $key=>$val){
              if (is_array($val)){
                  $retStr .= '<li>' . $key . ' => ' . pp($val) . '</li>';
              }else{
                  $retStr .= '<li>' . $key . ' => ' . $val . '</li>';
              }
          }
      }
      $retStr .= '</ul>';
      return $retStr;
  } 

  
  function getall($tablename, $conn){/*gets all of the results from $tablename */
    
    $query = "SELECT * FROM {$tablename}";
    if($results = mysqli_query( $conn , $query )){
      return $results;
    }
  }
  
  function addproject(){
    ?>
    <form method='post' action=''>
    <table class='newproject'>
      <tr>
        <td>Project Name</td>
        <td><input type='text' name='name'></td>
      </tr>
      <tr>
        <td>Language</td>
        <td><input type='text' name='language'></td>
      </tr>
      <tr>
        <td>About</td>
        <td><textarea name='about' rows='10' cols='50'></textarea></td>
      </tr>
      <tr>
        <td>Source Code</td>
        <td><textarea name='sourcecode' rows='10' cols='50'></textarea></td>
      </tr>
      <tr>
        <td>Pic Location</td>
        <td><input type='text' name='piclocation'></td>
      </tr>
      <tr>
        <td colspan="2"><input type="submit" name="newcode"></td>
      </tr>
    </table>
    <?php
    
  }
  
  function addcode($conn, $details){
    $qs = mysqli_prepare($conn, "INSERT INTO portfolio ( name, language, about, sourcecode, piclocation) VALUES (?,?,?,?,?)");
    mysqli_stmt_bind_param($qs, 'sssss', $details['name'],$details['language'],$details['about'],$details['sourcecode'],$details['piclocation']);
    mysqli_stmt_execute($qs);
}

    function deletecode($conn, $details){
        $qs = mysqli_prepare($conn, "DELETE FROM portfolio WHERE id=?");
        mysqli_stmt_bind_param($qs, 's', $details['deletecode']);
 
        mysqli_stmt_execute($qs);
        
    }
?>
