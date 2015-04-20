<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 22:14:32
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-20 00:17:20
 */
include_once 'htmlHeader.php';

class loggedHtmlBuilder{
    private $data = array();
    public function __construct()
    {
        # code...
    }
    public function generate_logged_in_page(){
        $this->logged_header();
        $this->logged_body();
    }
    private function display_newitem_form(){
        ?>
        <div class="newitemdiv">
            <form action="" method="POST" class="newitemform">
                <div class="newitemformInner">
                    <span class="itemformheader">New item</span>
                    <div class="itemshort">
                        <input class="newitemdescription" type="text" name="itemshort" />
                    </div>
                    <div class="itemlong">
                        <textarea class="itemnewtextarea"name="itemlong"></textarea>
                    </div>
                    <div class="itemsubmit">
                        <input type="hidden" value="<?php echo $_SESSION['uid']; ?>" name="uid">
                        <input class="newitemsubmit" type"submit" name="newitem" value="New item">
                    </div>
                </div>
            </form>
        </div>
        <?php
    }
    private function display_newtag_form(){
        ?>
        <div class="newtagdiv">
            <form action="" method="POST" class="newtagform">
                <div class="newtagformInner">
                    <span class="tagformheader">New tag</span>
                    <div class="tagshort">
                        <input class="newtagdescription" type="text" name="tagshort" />
                    </div>
                    <div class="taglong">
                        <textarea class="tagnewtextarea"name="taglong"></textarea>
                    </div>
                    <div class="tagsubmit">
                        <input type="hidden" value="<?php echo $_SESSION['uid']; ?>" name="uid">
                        <input class="newtagsubmit"type"submit" name="newtag" value="New tag">
                    </div>
                </div>
            </form>
        </div>
        <?php
    }
    private function logged_nav(){
      ?>
          <div id="navWrap">
              <div id="nav">
                  <ul>
                     <li><a class="smoothScroll" href="./?l">login</a></li>
                     <li><a class="smoothScroll" href="./?n">newUser</a></li>
                  </ul>    
                  <br class="clearLeft">
              </div>
          </div>
      <?php
    }
    private function logged_header(){
        ?>
        <div id="header">
            <?php
            $this->logged_nav();
            /*
            This is left open to easily add elements to this area.
            */
            ?>
        </div>
        <?php
    }
    private function left_half(){
        ?>
        <div class="newThings">
            <span class="newThingsSpan">Create a new</span>
            <div class="newItem">
                <?php $this->display_newitem_form(); ?>
            </div>
            <div class="newTag">
                <?php $this->display_newtag_form(); ?>
            </div>
        </div>
        <?php
    }

    private function logged_body(){
        ?>
        <div class="mainBody" id="mainBody">
            <div class="mainBodyLeft" id="mainBodyLeft">
                <?php $this->left_half(); ?>
            </div>
            <div class="mainBodyRight" id="mainBodyRight">
                <?php $this->right_half(); ?>
            </div>
        </div>
        <?php
    }
    private function right_half(){
        ?>
        <div class="newThings">
            <span class="newThingsSpan">Create a new</span>
            <div class="newItem">
                <?php $this->display_newitem_form(); ?>
            </div>
            <div class="newTag">
                <?php $this->display_newtag_form(); ?>
            </div>
        </div>
        <?php
    }
}