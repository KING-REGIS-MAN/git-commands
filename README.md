# Git Command

Git is an open source distributed version control system.

## The Stages of git
![](https://camo.githubusercontent.com/f92a0389b314ddf7cf48d9dd2b518bfa3e28933c8d88fc89e17ff7b3483d336a/68747470733a2f2f63646e2e686173686e6f64652e636f6d2f7265732f686173686e6f64652f696d6167652f75706c6f61642f76313634343837313636373732382f553875556b594951612e706e673f6175746f3d636f6d70726573732c666f726d617426666f726d61743d77656270)
-- The Wsorkspace: This is where unstaged files are located
-- The Staging Area: This is where files go to after the have been staged
-- The Commit/Local Rep: This where the commmited files are saved as a version
-- The Remote Repo: This is where the pushed local repo are stored remotely

## The commands
### Initializing a Repo
To initializa a Repo for an existing project,
-- Navigate to the working dir of the project you want to initialize and use the command
```sh
cd <project-dir>
git init
```

To initialize a Repo for an new project,
-- Create a repo on github and use the command 'git clone' to clone the repo locally and begin your project
```sh
git clone <repo--url>
```
### Checking the status of our file
To check the status of your files, you use command `git status`, this  will show you 
if your files are untracked, staged and ready for committing
```sh
git status
```
### Basic Snapshotting

| Command | Description |
| ------- | ----------- |
| `git status` | Check status |
| `git add [file-name.txt]` | Add a file to the staging area |
| `git add -A` | Add all new and changed files to the staging area |
| `git commit -m "[commit message]"` | Commit changes |
| `git rm -r [file-name.txt]` | Remove a file (or folder) |

### Branching & Merging

| Command | Description |
| ------- | ----------- |
| `git branch` | List branches (the asterisk denotes the current branch) |
| `git branch -a` | List all branches (local and remote) |
| `git branch [branch name]` | Create a new branch |
| `git branch -d [branch name]` | Delete a branch |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git checkout -b [branch name]` | Create a new branch and switch to it |
| `git checkout -b [branch name] origin/[branch name]` | Clone a remote branch and switch to it |
| `git branch -m [old branch name] [new branch name]` | Rename a local branch |
| `git checkout [branch name]` | Switch to a branch |
| `git checkout -` | Switch to the branch last checked out |
| `git checkout -- [file-name.txt]` | Discard changes to a file |
| `git merge [branch name]` | Merge a branch into the active branch |
| `git merge [source branch] [target branch]` | Merge a branch into a target branch |
| `git stash` | Stash changes in a dirty working directory |
| `git stash clear` | Remove all stashed entries |

### Sharing & Updating Projects

| Command | Description |
| ------- | ----------- |
| `git push origin [branch name]` | Push a branch to your remote repository |
| `git push -u origin [branch name]` | Push changes to remote repository (and remember the branch) |
| `git push` | Push changes to remote repository (remembered branch) |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git pull` | Update local repository to the newest commit |
| `git pull origin [branch name]` | Pull changes from remote repository |
| `git remote add origin ssh://git@github.com/[username]/[repository-name].git` | Add a remote repository |
| `git remote set-url origin ssh://git@github.com/[username]/[repository-name].git` | Set a repository's origin branch to SSH |

### Inspection & Comparison

| Command | Description |
| ------- | ----------- |
| `git log` | View changes |
| `git log --summary` | View changes (detailed) |
| `git log --oneline` | View changes (briefly) |
| `git diff [source branch] [target branch]` | Preview changes before merging |



<h1 align="center">Git workflow</h1> 
 
 <h3>Working directory</h3> 
 
```md
The actual file's states in the file system, they can be tracked or untracked, they can be changed or deleted.
```

 <h3>Staging area</h3> 
 
```md
The area where we prepared a set of files for a new version based its changes.
```

<h3>HEAD</h3> 

```md
It's the pointer in the current branch, it has the complete repository history.
```

### <h3>Remote Repo</h3> 

```md
In simple words its' just a space provided to share and collaborate your code with the community and frineds . 
```