<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 23:00:30
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-21 20:20:29
 */
include_once "functions.php";
function htmlHead(){
    ?>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
            Basic todo list for jlmarks
        </title>
        <script type="text/javascript" src="https://if188.infusionsoft.com/app/webTracking/getTrackingCode?trackingId=c7a7941f01a1106bc621716f90f98391"></script>
        <link rel='stylesheet' id='style-css'  href='http://i.jlmarks.org/style.css' type='text/css' media='all' />
        <link rel='stylesheet' id='style-css'  href='http://i.jlmarks.org/navbar.css' type='text/css' media='all' />
        <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
        <script type='text/javascript'>
        //<![CDATA[ 
        $(function() {
            // Stick the #nav to the top of the window
            var nav = $('#nav');
            var navHomeY = nav.offset().top;
            var isFixed = false;
            var $w = $(window);
            $w.scroll(function() {
                var scrollTop = $w.scrollTop();
                var shouldBeFixed = scrollTop > navHomeY;
                if (shouldBeFixed && !isFixed) {
                    nav.css({
                        position: 'fixed',
                        top: 0,
                        left: nav.offset().left,
                        width: nav.width()
                    });
                    isFixed = true;
                }
                else if (!shouldBeFixed && isFixed)
                {
                    nav.css({
                        position: 'static'
                    });
                    isFixed = false;
                }
            });
        });

        //]]>  
        </script>
    </head>
    <?php
}
function bodyStart(){
    ?>
    <body>
    <?php 
    include_once("analytics.pw.php");
}
function footer(){
}
function bodyEnd(){
    footer();
    ?>
    </body>
    <?php
}
function inboxSubmitter(){
    ?>
    <div class="newNote">
        <!-- http://requestb.in/oomdjaoo -->
    <!--         <div class="newNoteHeader">
            <h2>Leave a note!</h2>
        </div> -->
        <form method='post' action='' id='addNote' class="mobilePost">
            <div class="noteAndTagHolder">
                <div class="titleHolder">
                    <input type="text" name="noteText" id="noteText" />
                </div>
                <div class="noteArea">
                    <textarea name="notes" form="addNote" id="notes"> </textarea>
                </div>
                <div class="tagArea">
                    <?php
                    echo get_tags_as_option(); //because I will probably want to remove it on demand and use it elsewhere
                    ?>
                </div>
                <div class="mainSubmit">
                    <input class="mobilesubmit" type="submit" name="newItem" value="new note">
                </div>
            </div>
        </form>
    </div>
    <?php
}
function listAllNotes(){
    if (isset($_GET['a'])){
        $allnotes = get_all_notes();
        ?>
        <div id="allNotes">
            <table class="allNotes">
                <tr>
                    <td>id</td>
                    <td>text</td>
                </tr>
            <?php
            foreach ($allnotes as $key => $value) {
                $colorID = ($key%2==0 ? "even" : "odd");
                ?>
                <tr class="noteHolder <?php echo $colorID; ?>">
                    <td><a href="http://i.jlmarks.org/?editCatchall=<?php echo $key;?>"><?php echo $key;?></a></td>
                    <td><?php echo htmlspecialchars($value);?></td>
                </tr>
                <?php 
            } ?>
            </table>
        </div>
        <?php
    } elseif (isset($_GET['t'])) {
        tagCreationForm();
    } elseif (isset($_GET['ga'])){
        getNotesWithTags();
    }
}
function tagCreationForm(){
    if (isset($_GET['newTag'])){
        ?>
        <div id="newTagFormHolder" class="newForm mobilePost">
            <form id="newTagForm" action='' class="newForm" method="POST">
                <div id="newTagElements" class="tag">
                    <div class="tag display">
                        <label>
                            Tag Name:
                            <input type="text" name="newTagName">
                        </label>
                    </div>
                    <div class="tag description">
                        <textarea name="tagDescription" form="newTagForm">
                            Describe this tag, if you like.
                        </textarea>
                    </div>
                    <div class="tag submit">
                        <input type="SUBMIT" name="newTag" value="new tag">
                    </div>
                </div>
            </form>
        </div>
        <?php
    }
}
function getNotesWithTags(){
    $allnotes = get_all_notes();
    $alltags = get_all_tags();
    $allapplications = get_all_tagapplications();
    $notesWithTags=array();
    foreach ($allnotes as $key => $value) {
        $notesWithTags[$key] = array( "text" => $value, "tags" => array() );
    }
    foreach ($allapplications as $key => $value) {
        $notesWithTags[$value['catchallid']]["tags"][$value["catchalltagid"]] = $alltags[$value["catchalltagid"]];
    }
    ?>
    <div class="allNotesWithTags">
        <table class="allnotesAndTags">
            <?php
            $counter=1;
            foreach ($notesWithTags as $key => $value) {
                $rowValue = ( $counter++ % 2 == 0 ? "even" : "odd");
                ?>
                <tr class="noteRow <?php echo $rowValue; ?>">
                    <td class="noteID">
                        <a href="http://i.jlmarks.org/?editCatchall=<?php echo $key; ?>"><?php echo $key; ?></a>
                    </td>
                    <td class="noteText">
                        <?php echo htmlspecialchars($value['text']); ?>
                    </td>
                    <td class="tagHolder">
                        <?php
                        foreach ($value["tags"] as $tagid => $tagtext) {
                            ?>
                            <span id="<?php echo "tag" . $key . ":" . $tagid;?>" class='tag <?php echo $tagid;?>'>
                                <?php
                                echo $tagtext;
                                ?>
                            </span>
                            <?php
                        }
                        ?>
                    </td>
                </tr>
                <?php
            }
}
function editItem($editParams){
    // $editParams is expected to be an array with the layout of
    // $editParams['id'] = statement id that we are working with
    // $editParams['viewPort'] = optional argument that provides additional
    //      ways of viewing the data
    $properties=array();
    $properties['id']=$editParams['id'];
    $properties['catchallAll']=get_catchall_all($properties['id']);
    $properties['tagsApplied'] = get_tags_applied($properties['id']);
    $properties['alltags']=get_all_tags();
    $properties['tagidApplied']=array();
    // print_r($properties);
    ?>
    <div class="editItem" id="editItem<?php echo $properties['id']; ?>">
        <div class="manualUpdateLink">
            <span class="editLink">
                <a class="editLink" href="http://i.jlmarks.org/?editCatchall=<?php echo $properties['id']; ?>">edit</a>
            </span>
        </div>
        <form class="editItemForm" id="editItemForm<?php echo $properties['id']; ?>" action='./'  method='POST'>
            <div class="editName">
                <input type="text" name="catchallText" class="catchallText" value="<?php echo $properties['catchallAll']['text']; ?>">
            </div>
            <div class="updateHolder">
                <div class="editNotes">
                    <textarea class="noteTextArea" form="editItemForm<?php echo $properties['id']; ?>" id="notesFor<?php echo $properties['id']; ?>" name="notesArea"><?php echo ( isset($properties['catchallAll']['notes']) ? $properties['catchallAll']['notes'] : ""); ?></textarea>
                </div>
                <div class="appliedTags">
                    <?php
                    foreach ($properties['tagsApplied'] as $applicationId => $values) {
                        $displayText = $properties['alltags'][$values['catchalltagid']];
                        $properties['tagidApplied'][$values['catchalltagid']]=$displayText;
                        ?>
                        <label for="<?php echo $properties['id'] . "tag" . $values['catchalltagid']; ?>"  class="tag tag<?php echo $values['catchalltagid']; ?>" ><?php echo $displayText; ?></label><input type="checkbox" class="hiddenCheckbox" id="<?php echo $properties['id'] . "tag" . $values['catchalltagid']; ?>" name="<?php echo $properties['id']; ?>tag[]" value="<?php echo $values['catchalltagid'];?>" />
                        <?php
                    } ?>
                </div>
                <div class="addTagsDiv">
                        <?php 
                        foreach ($properties['alltags'] as $tagid => $displayText) {
                            if (!isset($properties['tagidApplied'][$tagid])){
                                ?>
                                <label for="<?php echo $properties['id'] . "tagtoapply" . $tagid; ?>"  class="tag tag<?php echo $values['catchalltagid']; ?>" ><?php echo $displayText; ?></label><input type="checkbox" class="hiddenCheckbox" id="<?php echo $properties['id'] . "tagtoapply" . $values['catchalltagid']; ?>" name="<?php echo $properties['id']; ?>tag[]" value="<?php echo $tagid;?>" />
                                <?php
                            }
                        } ?>
                </div>
            </div>
            <div class="breaker">
            </div>
            <div class="tabview">
            </div>
            <div class="submitButtonHolder">
                <input type="hidden" name="catchallid" value="<?php echo $properties['id']; ?>">
                <input type="submit" name="updateRecord" class="updateRecordSubmit" value="Update">
            </div>
        </form>
    </div>
    <?php
}