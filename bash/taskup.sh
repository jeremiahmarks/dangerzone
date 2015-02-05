#!/bin/sh
# @Author: jlmarks
# @Date:   2014-03-17 15:17:36
# @Last Modified by:   jlmarks
# @Last Modified time: 2014-03-17 16:00:20

/usr/local/bin/task sync
/usr/local/bin/task export > tasks.json
scp tasks.json bj:/var/www/html/task/tasks.json
