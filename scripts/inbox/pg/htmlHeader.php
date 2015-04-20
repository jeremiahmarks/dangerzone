<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-19 20:53:39
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-20 00:01:21
 */
?>
<head>
  <title>iinbox</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <script type="text/javascript" src="https://if188.infusionsoft.com/app/webTracking/getTrackingCode?trackingId=c7a7941f01a1106bc621716f90f98391"></script>
  <link rel='stylesheet' id='style-css'  href='style.css' type='text/css' media='all' />
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
<body>
