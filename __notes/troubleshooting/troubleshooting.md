




I really should be annotating troubleshooting that I am doing so when I need to reference it in the future, I have it available.

#Git
###I guess that I made changes last night and did not commit them.  Then, from a different computer I made several commits today.  I went to my home computer and attempted to pull and got the message
		
    error: Your local changes to the following files would be overwritten by merge:
    		path/to/fi.le
    Please, commit your changes or stash them before you can merge.
    Aborting

###Then I ran `git status` and got

    Your branch is behind 'origin/master' by 4 commits, and can be fast-forwarded.
      (use "git pull" to update your local branch)
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

##Resolution

###stash everything with `git stash -all`
###pull the latest down latest with `git pull`
###Returned to stash with `git stash apply`
###Used `git reset HEAD path/to/file` to take conflict file out of the commited changes
###(Added files that I did want to retrieve to the commit)
###Committed and pushed
###Got back out of the stash by creating a new one.
Seriously, though, find that answer
###Removed the stashes using `git stash drop stash@{X}`
