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
To check the status of your files, you use command `git status`, this  will show you if your files are untracked, staged and resdy for committing
```sh
git status
```