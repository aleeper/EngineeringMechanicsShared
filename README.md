READ ME!
=======

This repo contains materials for courses on vector geometry and mechanics,
e.g. engineering statics and dynamics, graphics, and robotics.
It has been used to teach ENGR 14/15 at Stanford, and ME 101 at SJSU.

##Initial Setup

###Install Prerequisites
The source material in this repo requires a working Latex distribution.
You will likely also want a TeX-aware text editor.

Note all of the helper scripts and build files assume the existence of `make`.

######Linux:
Issue the following commands at the terminal prompt:
```
sudo apt-get install texlive-latex-base  # Base latex packages.
sudo apt-get install texlive-extra-utils texlive-math-extra texlive-science
sudo apt-get install build-essential     # Installs make and other build tools.
# Optional:
sudo apt-get install texmaker
```
######Mac:
1. Download and install MacTeX from here: https://tug.org/mactex/
1. Install command-line tools. [These directions](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/) may be useful.
1. (Optional) Install a latex editor such as
[TeXMaker](http://www.xm1math.net/texmaker/download.html#macosx) or
[TeXShop](http://pages.uoregon.edu/koch/texshop/obtaining.html).


###Learn About Git
Make sure you have a basic understanding of git before you launch into things:

* [Quick In-Browser Git Tutorial](https://try.github.io/)
* [Simple Git Overview](http://rogerdudler.github.io/git-guide/)
* [Cheatsheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
* [Git Tips for SVN Users](http://www.davewentzel.com/content/git-gotchas-savvy-svnr)


###Clone This Repo
From the command line:
```
git clone https://github.com/aleeper/EngineeringMechanicsShared
```
Or, you may consider trying out the
[Github for Mac](https://mac.github.com/) desktop client.
(I don't use it, but I'm a purist.)


##Building
###Configuration
Each time you open a new terminal window that you will use for
building you must configure the build environment:
```
cd engineering_mechanics
source setup.sh
```
The configuration will persist until the terminal window is closed.

###Compiling Materials
The PDFs are built via `make`.
```
cd problems/coolExample/
make
```

This will produce two PDFs:

* coolExample-Student.pdf
* coolExample-Instructor.pdf

Some additional helpful make commands:

* `make view`  - Opens the two compiled PDFs for viewing.
* `make clean` - Deletes the compiled PDFs and temporary build files.

##Best Practices
This is a non-exhaustive list of some tips for working with LaTeX and git.

###Latex

* Break lines in the .tex file (that is, hit "Enter") after about 80 characters.
This does not affect the compiled output, but it makes it easier for line-based
editors and tools (like git!) to work with the file.
* Don't use tabs in the .tex file. Configure your text editor to use spaces
instead of tabs.

###Git
* Binary files (non-text, such as PDFs, images, and videos) cannot be "diff-ed",
meaning git must remember a new copy of the entire file even when the difference
from the previous version is very small. Hence, please avoid adding files that
will change often (such as the compiled output PDFs) or very large binary files
(videos) to the repository.
* Don't simply delete files which are being tracked by git. Instead use
`git rm -- file.txt` . You can usually do this even if you messed up and already
deleted the file. Note if you've made un-committed changes to the file it will
complain. You can **force** it to delete and forget about the file with `git rm -f -- file.txt`.

##Git Workflow
This repo roughly follows the guidelines
[set forth here](http://nvie.com/posts/a-successful-git-branching-model/)
except there is no "develop" branch. You should create feature branches off of master,
and then make pull requests against master.

#####A Simplified Summary for Working with Branches
While git is very powerful (and you should feel free to use any features you wish),
what follows are some instructions for a simplified workflow:

**Before starting to work,** fetch and merge any new changes from the remote:
```bash
git fetch origin --prune  # Fetches changes from the remote (github).

# If you don't yet have a feature branch:
git checkout -b my-branch origin/master  # Don't actually call it my-branch.

# If you already have a branch you are working with that is currently checked out:
git merge origin/master   # Merges latest master into your working branch.
```

**If there are conflicts** when you merge, resolve them
([see here](https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/) for info)
and then:
```bash
# (First manually fix any conflicting files.)
git add -- <fixed_file_1> <fixed_file_2>  # Adds changes to index.
git commit -m "manual merge"              # Commits the merge to your working branch.
```

**After doing work,** add and commit the changes locally, then push to the remote:
```
git add -- <file_1> <file_2>   # Add or "stage" changes in the index.
git commit -m "Message"        # Commit staged changes to your local working branch.
git push origin my-branch      # Push changes to the remote (github).
```

If the push succeeds, it will show something like:
>  4502166..a4a6c4d  my-branch -> my-branch

If it fails, it will show something like:
>  ! [rejected]        my-branch -> my-branch (fetch first)

If you see this, it means someone else has added changes to the remote copy of
your branch that are new since the last time you fetched.

**When you are ready for review and merging to master**,
make sure you have pushed the latest version of your branch:
```bash
git push origin my-branch
```

Then go on github and create a pull request, using "master" as the base branch.
