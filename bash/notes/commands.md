<!-- File Name: commands.md  -->
<!-- Author: Jeremiah Marks -->
<!-- Date:   2014-03-27 22:17:16 -->
<!-- Last Modified by:   Jeremiah Marks -->
<!-- Last Modified time: 2014-03-27 22:17:16 -->
<!-- Email: jeremiah@jlmarks.org-->
A list of commands, keywords, and variables used within either BASH scripting or on the command line. 

[a](#a)
***
[i](#i)
***

#[IFS](#ifs)
IFS stands for "internal field separator". This variable determines how bash recognizes
fields when it interprets character strings. ex:

```bash
var="'(]\\{}\$\""
echo $var        # '(]\{}$"
IFS='\'
echo $var        # '(] {}$"     \ converted to space.
```
***
[j](#j)
***
[k](#k)
***
[special Characters](#specchars)

#[\[](#leftbracket)
