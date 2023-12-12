Microsoft Windows [Version 10.0.22631.2428]
(c) Microsoft Corporation. All rights reserved.

C:\Users\asus 10th gen88>cd C:\Users\asus 10th gen88\Mypythonproject

C:\Users\asus 10th gen88\Mypythonproject>type nul > main.py

C:\Users\asus 10th gen88\Mypythonproject>git add main.py

C:\Users\asus 10th gen88\Mypythonproject>git commit -m "Initial commit"
[master 65fab68] Initial commit
 1 file changed, 1 deletion(-)

C:\Users\asus 10th gen88\Mypythonproject>git branch feature-branch
fatal: a branch named 'feature-branch' already exists

C:\Users\asus 10th gen88\Mypythonproject>git branch -D feature-branch
Deleted branch feature-branch (was 70635f0).

C:\Users\asus 10th gen88\Mypythonproject>git branch feature-branch

C:\Users\asus 10th gen88\Mypythonproject>git checkout feature-branch
Switched to branch 'feature-branch'

C:\Users\asus 10th gen88\Mypythonproject>