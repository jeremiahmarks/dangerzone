<?php
/**
 * @Author: Jeremiah Marks
 * @Date:   2015-04-20 21:37:29
 * @Last Modified by:   Jeremiah Marks
 * @Last Modified time: 2015-04-21 01:12:04
 */

// chop()  Removes whitespace or other characters from the right end of a string
// chunk_split()   Splits a string into a series of smaller parts
// explode()   Breaks a string into an array
// implode()   Returns a string from the elements of an array
// parse_str()     Parses a query string into variables
// similar_text()  Calculates the similarity between two strings
// strchr()    Finds the first occurrence of a string inside another string (alias of strstr())
// strrchr()   Finds the last occurrence of a string inside another string

// take string, 
//     explode into array. 
//     get last item of array
//     inspect element:
//         if firstChar = "#":
//             create tags based on item
//             if last item of array :
//                 remove from array
//         else
//             get next item.
include_once 'functions.php';
function splitOutTags( $sstring, $tarray=array() ){
    $sarray = explode(" ", $sstring);
    $fw = end($sarray);
    if ($fw[0]=="#"){
        $tarray[] = array_pop($sarray);
        $tarray = splitOutTags( implode( ' ', $sarray ), $tarray );
    } else {
        $tarray['finalString']=$sstring;
        while ($wordIn = prev($sarray)) {
            if ($wordIn[0] == "#"){
                $tarray[] = $wordIn;
            }
        }
    }
    return $tarray;
}

function parse_input($sstring){
    echo "WHAT WHAT";
    echo $sstring;
    $tags = splitOutTags($sstring);
    $finalString = $tags['finalString'];
    unset($tags['finalString']);
    $itemid=add_item($finalString);
    foreach ($tags as $key => $value) {
        if ($value[0]=="#"){
            $value = substr($value, 1);
        }
        $tagid=create_tag($value);
        apply_tag_to_item($itemid, $tagid);
    }
}

// $testStrings = array("Apple #red blue #This #that brown The#face #one #two", "#We #Ran #And #Ran");
// foreach ($testStrings as $key => $value) {
//     echo parse_input($value);
// }
?>