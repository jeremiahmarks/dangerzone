<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-18 15:04:19
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-18 16:16:43
 */
session_start();
include_once "../functions.php";
include_once '../htmlElements.php';

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
            if (isset($_SESSION['addTags'])){
                unset($_SESSION['addTags']);
            }
            if (isset($_SESSION['removeTags'])){
                unset($_SESSION['removeTags']);
            }
            foreach ($_SESSION['allTags'] as $tagid => $displayText) {
                if (isset($_SESSION['tagSearchTags'][$tagid])){
                    removeableTags($tagid, $displayText);
                } else {
                    addableTags($tagid, $displayText);
                }
            }
            ?>
            <div class="tagHolder">
                <div class="addableTags">
                    <?php
                    if (isset($_SESSION['addTags'])){
                        printArrayOfTags($_SESSION['addTags'], 'add');
                    }
                    ?>
                </div>
                <div class="removeableTags">
                    <?php
                    if (isset($_SESSION['removeTags'])){
                        printArrayOfTags($_SESSION['removeTags'], 'remove');
                    }
                    ?>
                </div>
            </div>
            <input type="submit" value='Update Tags' name='updateTagSearch'>
        </form>
    </div>
    <?php
}

function addableTags($tagid, $displayText){
    if (!isset($_SESSION['addTags'])){
        $_SESSION['addTags']=array();
    }
    $_SESSION['addTags'][$tagid]=array( 'tagid'=>$tagid, 'displayText' => $displayText );
}
function removeableTags($tagid, $displayText){
    if (!isset($_SESSION['removeTags'])){
        $_SESSION['removeTags']=array();
    }
    $_SESSION['removeTags'][$tagid]=array( 'tagid'=>$tagid, 'displayText' => $displayText );
}
function printArrayOfTags($arrayOfTags, $preName){
    foreach ($arrayOfTags as $key => $value) {
        ?>
        <label for="<?php echo $preName . $value['tagid']; ?>"  class="tag tag<?php echo $value['tagid']; ?>" >
            <?php echo $value['displayText']; ?>
        </label>
        <input type="checkbox" class="hiddenCheckbox" id="<?php echo $preName . $value['tagid']; ?>" name=<?php echo $preName . "tag[]";?> value="<?php echo $value['tagid'];?>" />
        <?php        
    }
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
        unset($_SESSION['tagSearchTags'][$catchalltagid]);
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
    if (isset($_POST['removetag'])){
        foreach ($_POST['removetag'] as $key => $value) {
            if (isset($_SESSION['tagSearchTags'][$value])){
                removeAllMatching($value);
            }
        }
    }
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
footer();
bodyEnd();