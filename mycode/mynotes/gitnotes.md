#Notes on using git.

##Start a new repo:  
1. navigate to the folder that you intend to use as the base of the project. 
2. run "git init" to create repo
3. run "git add ."  to add all items in folder to new repo.
4. run "git commit"  to be prompted to input commit message and update current files to the repo.

##[Adding project to GitHub](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line)
1. Create new repo on Github
2. cd to directory of project
3. Start a new repo.
4. Add and commit files
5. Get remote repo address from Github site.
6. run "git remote add origin Remote.Repo.Url"
7. run "git remote -v"
8. Push the changes to github
    1. run git push origin master

#Commands

##git status

Provide the status of the local git environment

##git stash

saves your files that are not in sync locally so that you can access them when you need them (This is a best understanding after a first read through.)

##git stash list

provides list of stashes saved

##git stash apply

reverts to most recently saved stash

##git stash apply stash@{incrementer}

not that I am not 100% sure but from how I read it it will generally default to the naming convention of stash@{incrementer} ex:(stash@{0}, stash@{1}, stash@{3})

##git stash --keep-index

do not stash what has already been staged

##git stash -u

this will include untracked files in the stash

##git stash --patch

prompts you for which changes to stash and which not to.

##git stash --all

safer alternative to `git clean`.  Where `git clean` deletes the changed file, this will stash it

##git clean

deletes all changed files. They are not stashed, they do not pass go, they do not collect anything.





