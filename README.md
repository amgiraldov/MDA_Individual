# MDA_Individual

Modern Data Analytics 


# Main Branch:

How to run the code:
1) It is suggested to run the jupyter notebooks sequentially, according to the numbering that goes with the name


## Structure

### Set up the virtual environment (or use conda environment --> see conda cheat sheet: https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf ) 

Create a new virtual environment. (Make sure you are inside the repository folder)
```
python -m venv .venv
```
Activate the environment you just created:
* Windows
```
cmd:        .venv\Scripts\activate.bat
powershell: .venv\Scripts\Activate.ps1  (Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)
```
* Linux
```
source .venv/bin/activate
```
Also, make sure pip has the most recent version.
```bash
pip install --upgrade pip
```
If you installed packages in your own environment, don't forget to update them such that everyone is on the same wavelength.
```bash
pip freeze > requirements.txt
```
Finally, install the requirements into the virtual environment.
```bash
pip install -r requirements.txt
```

## Useful commands

Install requirements file and or update it
```bash
pip install -r requirements.txt
pip freeze > requirements.txt
```

Check current state
```bash
git status
```

Show all branches in repo
```bash
git branch -a
```

New branch (-b creates a new one, without -b you just switch to this branch)
```bash
git checkout -b <new_branch> <parent_branch>
```
example: git checkout -b featureX develop

Push new branch to remote repo
```bash
git push -u origin <new_branch>
```
example: git push -u origin featureX

When finished go to develop branch
```bash
git checkout develop
```

Merge feature into develop
```bash
git merge featureX
```

Delete branch locally
```bash
git branch -d localBranchName
```

Delete branch remotely
```bash
git push origin --delete remoteBranchName
```

Remove last commit
Remove it locally
```bash
git reset HEAD^
```

Eemove it remotely (you still have the file in work dir, so it's best to remove repo and start over)
```bash
git push origin +HEAD
```

(later if you want to pull/push)
```bash
git pull

git add .
git commit -m "text"
git push
```


