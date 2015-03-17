<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-03-15 10:32:56
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-03-15 16:22:28
 */
// include_once 'functions.php';
function headerStart(){
    ?>
    <head>
        <link rel='stylesheet'   href='./style.css' type='text/css' media='all' />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js "></script>
        <script>
            $.fn.serializeObject = function()
            {
                var o = {};
                var a = this.serializeArray();
                $.each(a, function() {
                    if (o[this.name] !== undefined) {
                        if (!o[this.name].push) {
                            o[this.name] = [o[this.name]];
                        }
                        o[this.name].push(this.value || '');
                    } else {
                        o[this.name] = this.value || '';
                    }
                });
                return o;
            };
        </script>
    </head>
    <?php
}

function bodyStart(){
    ?>
    <body class="statementSheet">
    <?php
}
function bodyEnd(){
    ?>
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
                url: 'index.php',
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


function tagSelector($tagsToSkip){
    ?>
    <select class="tagSelector" multiple size="5">
        <?php
        foreach ($_SESSION['tags'] as $key => $value) {
            if (!isset($tagsToSkip[$key])){
                ?>
                <option value="<?php echo $key; ?>">
                    <?php echo $value; ?>
                </option>
                <?php
            }
        }
        ?>
    </select>
    <?php
}

function unappliedTags($tagsToSkip){
    foreach ($_SESSION['tags'] as $key => $value) {
        if (!isset($tagsToSkip[$key])){
            // echo "adding unapplied tag because of " . $key;
            ?>
            <label class="tag unapplied">
                <?php echo $value; ?>
                <input type="checkbox" name="tagAdd[]" value="<?php echo $key; ?>" class="tag unapplied hidden">
            </label>
            <?php
        }
    }
}

function interiorInfo($statementID){
    ?>
    <form action="" method="POST" id="form<?php echo $statementID; ?>">
            <div class="statementWithTagsInterior" id="stmt<?php echo $statementID; ?>">
                <input type="hidden" name="statementID" value="<?php echo $statementID; ?>">
                <div class="statement">
                    <?php echo $_SESSION['statements'][$statementID]; ?>
                </div>
                <div class="appliedTags">
                    <?php
                    foreach ($_SESSION['stmtsToTags'][$statementID] as $key => $value) {
                        $skipTags[$value] = $value;
                        ?>
                        <label class="tag applied">
                            <?php echo $_SESSION['tags'][$value]; ?>
                            <input type="checkbox" name="tagRemove[]" value="<?php echo $value; ?>" class="tag applied hidden">
                        </label>
                        <?php
                    }
                    ?>
                </div>
                <div class="editOptions">
                    <?php
                    unappliedTags($skipTags);
                    ?>
                </div>
                <div class="actions">
                    <input type="submit" value="updateTags" class="updateTags">
                </div>
            </div>
        </form>
        <?php
}

function addStatementWithTags($statementID){
    $skipTags=array();
    ?>
    <div class="statementWithTags" id="<?php echo $statementID; ?>">
        <?php interiorInfo($statementID); ?>
    </div>
    <?php
    addAJAXScript($statementID);
}