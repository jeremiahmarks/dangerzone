from: https://help.ubuntu.com/community/CronHowto


Using Cron

To use cron for tasks meant to run only for your user profile, add entries to your own user's crontab file. Start the crontab editor from a terminal window:

crontab -e
N
Edit the crontab using the format described in the next sections. Save your changes. (Exiting without saving will leave your crontab unchanged.)

Note that a great source of information about the format can be found at:

man 5 crontab

Commands that normally run with administrative privileges (i.e. they are generally run using sudo) should be added to the root user's crontab (instead of the user's crontab):

 sudo crontab -e

Crontab Sections

Each of the sections is separated by a space, with the final section having one or more spaces in it. No spaces are allowed within Sections 1-5, only between them. Sections 1-5 are used to indicate when and how often you want the task to be executed. This is how a cron job is laid out:

minute (0-59), hour (0-23, 0 = midnight), day (1-31), month (1-12), weekday (0-6, 0 = Sunday), command

01 04 1 1 1 /usr/bin/somedirectory/somecommand

The above example will run /usr/bin/somedirectory/somecommand at 4:01am on January 1st plus every Monday in January. An asterisk (*) can be used so that every instance (every hour, every weekday, every month, etc.) of a time period is used. Code:

01 04 * * * /usr/bin/somedirectory/somecommand

The above example will run /usr/bin/somedirectory/somecommand at 4:01am on every day of every month.

Comma-separated values can be used to run more than one instance of a particular command within a time period. Dash-separated values can be used to run a command continuously. Code:

01,31 04,05 1-15 1,6 * /usr/bin/somedirectory/somecommand

The above example will run /usr/bin/somedirectory/somecommand at 01 and 31 past the hours of 4:00am and 5:00am on the 1st through the 15th of every January and June.

The "/usr/bin/somedirectory/somecommand" text in the above examples indicates the task which will be run at the specified times. It is recommended that you use the full path to the desired commands as shown in the above examples. Enter which somecommand in the terminal to find the full path to somecommand. The crontab will begin running as soon as it is properly edited and saved.

You may want to run a script some number of times per time unit. For example if you want to run it every 10 minutes use the following crontab entry (runs on minutes divisible by 10: 0, 10, 20, 30, etc.)

*/10 * * * * /usr/bin/somedirectory/somecommand

which is also equivalent to the more cumbersome

0,10,20,30,40,50 * * * * /usr/bin/somedirectory/somecommand