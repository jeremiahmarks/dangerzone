<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-17 23:27:51
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-18 14:47:43
 */
session_start();
include_once "functions.php";
include_once 'htmlElements.php';

## purpose:  to allow a user to select particular tags that 
## they are interested in and to show all items which have 
## those tags

function getAllTags(){
    if (isset($_SESSION['allTags'])){
        unset($_SESSION['allTags']);
    }
    $_SESSION['allTags'] = get_all_tags();
    ?>
    <div class="floatingTags">
        <form id='tagsToSearchFor' action='' method='POST'> 
            <?php
            foreach ($_SESSION['allTags'] as $tagid => $displayText) {
                ?>
                <label for="<?php echo "tagToAddToSearch" . $tagid; ?>"  class="tag tag<?php echo $tagid; ?>" >
                    <?php echo $displayText; ?>
                </label>
                <input type="checkbox" class="hiddenCheckbox" id="<?php echo "tagToAddToSearch" . $tagid; ?>" name="addtag[]" value="<?php echo $tagid;?>" />
                <?php
            } ?>
            <input type="submit" value='Update Tags' name='updateTagSearch'>
        </form>
    </div>
    <?php
}

function resetS(){
    if (isset($_SESSION['tagSearchTags'])){
        unset($_SESSION['tagSearchTags']);
    }
    if (isset($_SESSION['results'])){
        unset($_SESSION['results']);
    }

}

function addTagToCatchall($catchallid, $catchalltagid){
    if (!isset($_SESSION['results'])){
        $_SESSION['results'] = array();
    }
    if (!isset($_SESSION['results'][$catchallid])){
        $_SESSION['results'][$catchallid]=array( 'use' => 0, 'tags' => array() );
    }
    $_SESSION['results'][$catchallid]['use']++;
    $_SESSION['results'][$catchallid]['tags'][$catchalltagid]=$_SESSION['allTags'][$catchalltagid];
}
function removeTagFromCatchall($catchallid, $catchalltagid){
    if (isset($_SESSION['results'][$catchallid]['tags'][$catchalltagid])){
        unset($_SESSION['results'][$catchallid]['tags'][$catchalltagid]);
        $_SESSION['results'][$catchallid]['use']--;
    }
    if (isset($_SESSION['results'][$catchallid]['use'])){
        if ($_SESSION['results'][$catchallid]['use']<=0){
            unset($_SESSION['results'][$catchallid]);
        }
    }
}

function sortResults(){
    if (isset($_SESSION['results'])){
        foreach ($_SESSION['results'] as $idAsKey => $idData) {
            $numberOfUses[$idAsKey] = $idData['use'];
            $theseTags[$idAsKey] = $idData['tags'];
        }
        array_multisort($numberOfUses, SORT_DESC, $theseTags, SORT_ASC, $_SESSION['results']);
    }
}

function getAllMatching($catchalltagid){
    if (!isset($_SESSION['tagSearchTags'])){
        $_SESSION['tagSearchTags'] = array();
    }
    $_SESSION['tagSearchTags'][$catchalltagid]=get_all_catchalls_with_tag($catchalltagid);
    // $getAllStmt = "SELECT id, catchallid, catchalltagid FROM catchalltagapplications WHERE catchalltagid = ? ";
    // $_SESSION['tagSearchTags'][$catchalltagid][$id] = array($catchallid, $catchalltagid);
    foreach ($_SESSION['tagSearchTags'][$catchalltagid] as $id => $pairing ) {
        addTagToCatchall($pairing[0],$pairing[1]);
    }
}

function removeAllMatching($catchalltagid){
    if (isset($_SESSION['tagSearchTags'][$catchalltagid])){
        foreach ($_SESSION['tagSearchTags'][$catchalltagid] as $id => $pairing) {
            removeTagFromCatchall($pairing[0],$pairing[1]);
        }
    }
}

function printResults(){
    ?>
    <div class="resultsDiv">
        <?php
        if (isset($_SESSION['results'])){
            foreach ($_SESSION['results'] as $key => $value) {
                editItem(array( 'id' => $key ));
            }
        }
        ?>
    </div>
    <?php
}

if (isset($_POST['updateTagSearch'])){
    if (isset($_POST['addtag'])){
        foreach ($_POST['addtag'] as $key => $value) {
            getAllMatching($value);
        }
    }
    if (isset($_POST['removeTag'])){
        foreach ($_POST['removeTag'] as $key => $value) {
            if (isset($_SESSION['tagSearchTags'][$value])){

            }
        }
    }
}
if (isset($_POST)){
    echo pp($_POST);
}



htmlHead();
bodyStart();
getAllTags();
// getAllMatching(1);
// getAllMatching(3);
// getAllMatching(2);
// getAllMatching(4);
// sortResults();
printResults();
echo "<br /><br /><br /><br /><br />";
echo pp($_SESSION['results']);
echo "<br /><br /><br /><br /><br />";
footer();
bodyEnd();