<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-18 17:32:03
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-18 18:02:31
 */
include_once '../functions.php';

function myHeader(){
    ?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js'></script>
        <meta charset="utf-8">
        <!-- <link rel='stylesheet' id='style-css'  href='http://i.jlmarks.org/style.css' type='text/css' media='all' />
        <link rel='stylesheet' id='style-css'  href='http://i.jlmarks.org/navbar.css' type='text/css' media='all' /> -->
        <link rel='stylesheet' id='style-css'  href='./floating1.css' type='text/css' media='all' />
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

function bodystart1(){
    ?>
    <body>
       <div id="header">
            <div id="navWrap">
                <div id="nav">
                    <ul>
                        <li><a href="#" class="smoothScroll">Demo Link 1</a></li>
                        <li><a href="#" class="smoothScroll">Demo Link 2</a></li>
                        <li><a href="#" class="smoothScroll">Demo Link 3</a></li>
                        <li><a href="#" class="smoothScroll">Demo Link 4</a></li>
                    </ul>    
                    <br class="clearLeft" />
                </div>
            </div>
        </div>
        <?php
}
myHeader();
bodystart1();
inboxSubmitter();
listAllNotes();
tagCreationForm();
footer();
bodyEnd();
