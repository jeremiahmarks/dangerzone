#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-14 18:10:36
# @Last Modified 2015-03-14>
# @Last Modified time: 2015-03-14 20:18:11


####################################
## General Approach:
    ##  connect to mysql server
    ##  check if there filename with the same name
    ##      if there is, update the name with filename.before.DateTime
    ##  create a file in ~/webanize.py with the name of 
        ##  filename.DateTime(.html?)
    ##  write the correct header information into the file based
        ##  on filetype
    ##  write the file information formatted correctly into the file
    ## close the file
    ## prompt the user for the description information (include the old, if it exists)
    ## create an entry in the database for the file
