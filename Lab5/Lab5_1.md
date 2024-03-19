# Lab 5
## Part 1: Software Version Control with Git
### Prep:
- Launch DEVASC VM
- Open the terminal

```bash
git config --global user.name "<SampleUser>"
```
```bash
git config --global user.email "<sample@example.com>"
```
>[!Note]
> Change `<SampleUser>` to a username of choice \
> Change `<sample@example.com>` to the chosen username followed by `@example.com`

Lets take a look at the results
```bash
git config --list
```

### Create repository
```bash
cd labs/devnet-src/
mkdir git-intro
cd git-intro
git init
```

Check on the repository you just made:
```bash
ls -a
git status
```

### Staging and Committing
#### Prep
```bash
echo "I am on my way to passing the
Cisco DEVASC exam" > DEVASC.txt
ls -la
cat DEVASC.txt
git status
```
>[!Note]
>Look at the result of `git status`. Do you see `use "git add" to track`? That is what we are going to use next.

#### Staging
This part creates a snapshot of the file. So every change after needs another `git add` command.
```bash
git add DEVASC.txt
git status
```
>[!Note]
>Look at the result of `git status`. It's different now.

#### Committing
By committing we let Git know we want to track changes made to the file. We can give messages at every commit to clarify the change.
```bash
git commit -m "Committing
DEVASC.txt to begin tracking changes"
```
>[!Important]
>Notice the respons, every commit has a unique key. We can use this later.

Lets take a look at the log we just created:
```bash
git log
```

### Modifying and Tracking
#### Modifying
```bash
echo "I am beginning to understand
Git!" >> DEVASC.txt
cat DEVASC.txt
git status
```

As mentioned before, every change needs to be staged before it can be committed.
```bash
git add DEVASC.txt
git commit -m "Added additional
line to file"
```
>[!Tip]
>Notice the commit key.

Lets take a look at the changes:
```bash
git log
```
To look at the differences between commitments use the commit keys:
```bash
git diff <key1> <key2>
```
>[!Tip]
>If you haven't noticed yet, the key is represented as the first 7 characters in the commit in the log.

### Branches and Merging
#### Branches
Make and check a branch:
```bash
git branch feature
git branch
```
Switch to the branch and make sure you're switched:
```bash
git checkout feature
git branch
```
Modify the file from the new branch:
```bash
echo "This text was added
originally while in the feature branch" >> DEVASC.txt
cat DEVASC.txt
```

#### Merging
As before stage and commit the change:
```bash
git add DEVASC.txt
git status
git commit -m "Added a third line
in feature branch"
git log
```

Switch back to the master branch:
```bash
git checkout master
git branch
```

Merge the file contents and delete the feature branch:
```bash
git merge feature
cat DEVASC.txt
git branch -d feature
git branch
```
### Merge conflicts
#### prep
First we'll make a branch again and make some changes in the new branch. Then we are going to make a different change at the master branch to create a conflict.
```bash
git branch test
git checkout test
sed -i 's/Cisco/NetAcad/' DEVASC.txt
git commit -a -m "Change Cisco to
NetAcad"
git checkout master
sed -i 's/Cisco/DevNet/' DEVASC.txt
git commit -a -m "Changed Cisco to
DevNet"
```
#### merge
Now that the preperations are completed, try to merge `test` with `master`.
```bash
git merge test
```
>You've gotten a conflict on the content of DEVASC.txt \
>Now how do we solve this? \
>We know now what we did to cause this conflict but what if it isn't clear? Let's solve it.

Check the log for possible causes:
```bash
git log
```
>[!Note]
>`HEAD` is the representation of the master branch.

Check the file:
```bash
cat DEVASC.txt
```
>[!Note]
>Notice the part between `<<<<<<<<<<<<<<` and `>>>>>>>>>>>>>>`

Delete the unwanted data in the file:
VIM:
```bash
vim DEVASC.txt
```
Nano:
```bash
nano DEVASC.txt
```

Now try merging again:
```bash
git add DEVASC.txt
git commit -a -m "Manually merged
from test branch"
git log
```

### Integrate Git with GitHub
#### prep
>[!Warning]
>This step is not in the terminal!

- Create a GitHub account
- Log into GitHub
- Create a repository with:
    - Name 
        ```   devasc-study-team
        ```
    - Description
        ```   Working together to pass the DEVASC exam
        ```
    - Public/Private \
        `Private`

Go back to the terminal and prepare the local enviroment:
```bash
cd ~/labs/devnet-src/git-intro
mkdir devasc-study-team
cd devasc-study-team
cp ../DEVASC.txt .
```
Initialize git:
```bash
git init
git config --list
```
>[!Important]
>Notice that we are still using the local user we made in the first steps of the lab. We'll change this to match the online account.

```bash
git config --global user.name "<GitHub username>"
```
```bash
git config --global user.name "<GitHub email-address>"
```

#### Point Git to GitHub
```bash
git remote add origin https://github.com/<github-username>/devasc-study-team.git
```

Stage and commit DEVASC.txt

```bash
git add DEVASC.txt
git commit -m "Add DEVASC.txt file to devasc-study-team"
git log
git status
```
Push the file:
>[!Important]
>Before we push the file we need to create a token in GitHub. This replaces the password input when pushing.

Go to GitHub
 https://github.com/settings/tokens

 create a token (full repo scope)

```bash
git push origin master
```
- Username: `<GithubUsername>`
- Password: `<token>`

>[!Warning]
>: If, after entering your username and password, you get a fatal error stating repository is not found,
you most likely submitted an incorrect URL. You will need to reverse your git add command with the git
remote rm origin command.

Go to GitHub and verify:
- Repository
    - devas-study-team
        - DEVSASC.txt
