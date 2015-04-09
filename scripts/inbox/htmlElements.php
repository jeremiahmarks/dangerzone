<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-08 23:00:30
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-08 23:55:56
 */
include_once "functions.php";
function htmlHead(){
    ?>
    <head>
        <meta name="viewport" content="width=device-width" />
        <title>
            Basic todo list for jlmarks
        </title>
        <script type="text/javascript" src="https://if188.infusionsoft.com/app/webTracking/getTrackingCode?trackingId=c7a7941f01a1106bc621716f90f98391"></script>
        <link rel='stylesheet' id='style-css'  href='./style.css' type='text/css' media='all' />
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
        <form method='post' action=''>
            <table class='newNoteTable'>
                <tr>
                    <td colspan="2"><h2>Leave a note!</h2></td>
                </tr>
              <tr>
                <td>Note:</td>
                <td><input type='text' name='noteText'></td>
              </tr>
              <tr>
                <td colspan="2"><input type="submit" name="newItem" value="new note"></td>
              </tr>
            </table>
        </form>
    </div>
    <?php
}

function listAllNotes(){
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
                <td><?php echo $key;?></td>
                <td><?php echo $value;?></td>
            </tr>
            <?php 
        } ?>
        </table>
    </div>
    <?php

}