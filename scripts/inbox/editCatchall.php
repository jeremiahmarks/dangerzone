<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-18 20:55:47
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-19 03:13:44
 */
include_once 'htmlElements.php';
include_once 'functions.php';

class catchallRecord{
    private $id;
// $catchallAll['catchallid'] = $catchallid;
// $catchallAll['text']=$text;
// $catchallAll['created']=$created;
// $catchallAll['notes']=$notes;
    //get_tags_applied($catchallid);
// $stmtString = "SELECT id, catchalltagid, applied FROM catchalltagapplications WHERE catchallid = ?";
// mysqli_stmt_bind_result($stmt, $id, $catchalltagid, $applied);
// $allTagsAppliedData[$id] = array( 'catchalltagid' => $catchalltagid, 'applied' => $applied);
    private $text;
    private $created;
    private $notes;
    private $tags = array();
    public function __construct($catchallid){
        $this->id = $catchallid;
        $catchAllAll=get_catchall_all($catchallid);
        $this->text=$catchAllAll['text'];
        $this->created=$catchAllAll['created'];
        $this->notes=$catchAllAll['notes'];
        $this->tags['all'] = get_all_tags();
        $this->tags['applied'] = get_tags_applied($this->id);
        foreach ($this->tags['applied'] as $key => $value) {
            $this->tags['appliedByTagid'][$value['catchalltagid']] = array( 'tagid'=>$value['catchalltagid'], 'displayText'=>$this->tags['all'][$value['catchalltagid']]);
        }
        $this->tags['notApplied'] = array();
        foreach ($this->tags['all'] as $catchalltagid => $displayText) {
            if (!isset($this->tags['appliedByTagid'][$catchalltagid])){
                $this->tags['notApplied'][$catchalltagid]= array( 'tagid'=>$catchalltagid, 'displayText'=>$displayText );
            }
        }
        // foreach ($this->tags['notApplied'] as $key => $value) {
        //     $this->tags['notApplied'][$key]['displayText'] = $this->tags['all'][$value['catchalltagid']];
        // }
    }
    public function printRecords(){
        ?>
        <div class="recordsHolder">
            <div class="editRecord editRecord<?php echo $this->id; ?>">
                <form class="editIndivRecord editIndivRecord<?php echo $this->id; ?>" action="" method="post" name="editIndivRecord<?php echo $this->id; ?>" id="editIndivRecord<?php echo $this->id; ?>">
                    <div class="editName">
                        <input type='hidden' name="catchallTextOriginal" value="<?php echo $this->text; ?>" />
                        <input type="text" name="catchallText" class="catchallText" value="<?php echo $this->text; ?>" />
                    </div>
                    <div class="editTimestamp">
                        <span class="createdTimestamp">created: <?php echo $this->created; ?></span>
                    </div>
                    <div class="editNotesArea">
                        <input type='hidden' name="notesAreaOriginal" value="<?php echo $this->notes; ?>" />
<textarea class="noteTextArea" form="editIndivRecord<?php echo $this->id; ?>" id="notesFor<?php echo $this->id; ?>" name="notesArea">
<?php echo $this->notes; ?>
</textarea>
                    </div>
                    <div class="tagsHolder">
                        <div class="tagsApplied">
                            <input type="checkbox" name="appliedTags" id="appliedTags" class="tagThing hiddenCheckbox">
                            <label class="appliedTagsLabel" for="appliedTags">Applied</label>
                            <?php
                            print_array_of_tags($this->tags['appliedByTagid'], "appliedT");
                            ?>
                        </div>
                        <div class="tagsAvailable">
                            <input type="checkbox" name="availableTags" id="availableTags" class="tagThing hiddenCheckbox">
                            <label class="availableTagsLabel" for="availableTags">Available</label>
                            <?php
                            print_array_of_tags($this->tags['notApplied'], "availableT");
                            ?>
                        </div>
                    </div>
                    <div class="editSubmit">
                        <input type="hidden" name="catchallid" value="<?php echo $this->id; ?>">
                        <input type="submit" class="editCatchallSubmit" name="editCatchallSubmit" value="update record">
                    </div>
                </form>
                <div class="tabsHolder">
                    <!--basically a place to enable tabs at a later point. -->
                </div>
            </div>
        </div>
        <?php
    }
}

function collectDataAbout($catchallid){
    $catchAllAll=get_catchall_all($catchallid);
    $appliedTags=get_tags_applied($catchallid);
}
if ( isset ( $_GET['editCatchall'] ) ){
    $catchallRecord = new catchallRecord($_GET['editCatchall']);
    $catchallRecord->printRecords();
}
