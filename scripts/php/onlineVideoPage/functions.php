<?php
require 'my.pw.php';
/**
 * @Author: jeremiah.marks
 * @Date:   2015-02-17 14:23:45
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-02-18 01:40:32
 */
$conn =  mysqli_connect($dbpath, $dbuser,$dbpassword,$dbtouse);
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}
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

function nspp($arr){
  $retStr = '[';
  if (is_array($arr)){
    foreach ($arr as $key=>$val){
      if (is_array($val)){
        $retStr .= '[' . $key . ':' . nspp($val) . ']';
      } else {
        $retStr .= '[' . $key . ':' . $val . ']';
      }
    }
  }
  $retStr .= ']';
  return $retStr;
}

function addtodo($todotoadd) {
    //This function will be used to add todo items to the proper tables.
    global $conn;
    $toadd = mysqli_prepare($conn, "INSERT INTO inbox ( item, class) VALUES (?,?)");
    $class='todo';
    mysqli_stmt_bind_param($toadd, 'ss', $todotoadd, $class);
    mysqli_stmt_execute($toadd);
    $testa = $todotoadd . "todo";
    return $testa;
}

function insertScript($videoUrl){
  ?>
      <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js"></script>
    <script type="text/javascript">
      var flashvars = {};
      var params = {};
      var attributes = {};
      swfobject.embedSWF("<?php echo $videoUrl ?>.swf", "myAlternativeContent", "100%", "100%", "9.0.0", false, flashvars, params, attributes);
    </script>
<?php
}

function get_tables(){
  global $conn;
  $tableList = array();
  $res = mysqli_query($conn,"SHOW TABLES");
  while($cRow = mysqli_fetch_array($res))
  {
    $tableList[] = $cRow[0];
  }
  echo pp($tableList);
}

// function make_new_table($tablename, $column_names){
//   global $conn;
//   $cars = "CREATE TABLE cars(
//     carid int(10) NOT NULL auto_increment,
//     carowner int(11) NOT NULL,
//     make varchar(255),
//     model varchar(255),
//     plates varchar(255) NOT NULL UNIQUE,
//     PRIMARY KEY (carid)
//     )";
//   $vids = "CREATE TABLE vids(
//     vidid int(10) NOT NULL auto_increment,
//     name varchar(255),

//                              )
// }

function add_video_to_database($name){
  global $conn;
  $error='';
  $stmt = "INSERT INTO vids (name) VALUES ('" . $name . "')";
  $res = mysqli_query($conn,$stmt);
  $dataList = array();
  // while($cRow = mysqli_fetch_array($res)){
  //   $dataList[] = $cRow[0];
  // }
  echo $stmt;
  echo $res;
  echo pp($dataList);
}

function update_videos_by_name($name){
  global $conn;
  if ($stmt = mysqli_prepare($conn, "SELECT 'id' FROM 'vids' WHERE 'name' LIKE '?'")){
    echo "in the if";
    mysqli_stmt_bind_param($stmt, $name);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_bind_result($stmt, $vid);
    mysqli_stmt_close($stmt);
  }
  echo "hello";
  echo $stmt;
  echo pp($vid);

}
