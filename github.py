# initializes git repository on local machine lets github knows where does he want to accpet push req and pull req 
"git init"

"**git rev-parse --is-inside-work-tree" - "returns true on CLI if the current folder or dir is a git repository "

# GIT ADD 
'git add .' - 'adds all file in a current directory and not outside of it '
'git add -A' - 'adds all file in a git repo even if u r not at the root folder of the directory'
'git add -u ' - 'adds only the modified,tracked files and not the untracked '
'git add file1.txt file2.js dir/file3.py' - 'manually lets git know which files to add'
'git add -p' 


# git add -p
"""
diff --git a/README.md b/README.md
index e69de29..3b18e13 100644
--- a/README.md
+++ b/README.md
@@ -1 +1 @@
-# My Project
+# My Awesome Project
Stage this hunk [y,n,q,a,d,/,e,?]?


Imagine you changed 20 lines in README.md, but you only want to commit the first 5 lines (say, typo fixes) and leave the rest (say, experimental notes).
git add -p lets you commit just the important part and ignore the rest for now.
"""

# GIT COMMIT RESET - 03 ways( soft,reset , hard)

"1.git reset --soft HEAD~1"
'soft' - 'If you committed but realize “oops, I forgot to add one more file” or “wrong message”:'
"""
git commit -m "wrong message"
git reset --soft HEAD~1
git commit -m "correct message"
"""

"2.git reset HARD~1"
"Puts your files back into unstaged changes (like you just edited them)."

"3.git reset --hard HEAD~1"
'If you want to throw away the commit and all file changes:'


# check main and remote branch differecen
"git log HEAD..origin/main --oneline" - 'check how many commit your local/remote brach is ahead and behind to eachother'








# Undo a commit thats already pushed to github
'1.git revert <commit id>'
'Creates a new commit that "cancels out" the old one.'

""" Git Branching  """

# New branch create
"git branch feature/cart"

# Switch to branch
"git checkout feature/cart"

# Create & switch together
"git checkout -b feature/cart"

# Delete branch
"git branch -d feature/cart"

# Remote branch track
"git checkout -b feature/cart origin/feature/cart"

# See all branches
"git branch -a"



""" FAST FORWARD - NON_FAST_FORWARD """
# Remote  = A---B---C (origin/main)
# lcoal = A---B  (main)

"git pull origin/main"


# Remote  = A---B---C (origin/main)
# lcoal = A---B---D  (main)

'merge or rebase'
"""
git fetch origin
git merge origin/main   # extra merge commit banega
git push origin main
"""



num = 153
print(str(153))

