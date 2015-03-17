<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-03-15 14:44:10
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-03-15 15:10:49
 */
function pp($arr){ /*pretty print*/
//Provides a pretty way to see what an array contains. 
//Also is a recursive function.  
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

function regPage(){
    ?>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js "></script>
</head>

<body>
    <div id="1">
    <form action="" method="POST" id="form1">
        <div>
            <input type="hidden" name="1" value="two">
            <input type="hidden" name="2" value="two">
            <input type="submit" name="submit" value="T">
        </div>
    </form>
    <?php
    addAJAXScript(1);
    ?>
    </div>
</body>
<?php
}

function addAJAXScript($statementID){
    ?>
    <script>
    $(document).ready(function(){
        $("<?php echo "#form" . $statementID; ?>").submit(function(){
         
            // show that something is loading
            $('<?php echo "#" . $statementID; ?>').html("<b>Loading response...</b>");
             
            /*
             * 'post_receiver.php' - where you will pass the form data
             * $(this).serialize() - to easily read form data
             * function(data){... - data contains the response from post_receiver.php
             */
            $.ajax({
                type: 'POST',
                url: 'i2.php',
                data: $(this).serialize()
            })
            .done(function(data){
                 
                // show the response
                $('<?php echo "#" . $statementID; ?>').html(data);
                 
            })
            .fail(function() {
             
                // just in case posting your form failed
                alert( "Posting failed." );
                 
            });
     
            // to prevent refreshing the whole page page
            return false;
     
        });
    });
    </script>
    <?php
}

if (isset($_POST['form1'])){
    echo "noReg";
    return pp($_POST);
}else{
    echo "Reg";
    echo pp($_POST);
    regPage();
}
