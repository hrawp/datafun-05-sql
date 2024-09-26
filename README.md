


# datafun-05-sql
SQL work with Python

## I run db_initialize_aaron.py 
This sets up the database and pulls in data from two csv files authors and books.

## Next I run db_operations_aaron.py

This has what imports we need at the top.

## I define logging then setup all the diffrent file paths to the .sql files.

(images/Define1.jpg)

## Then I define the functions which call the .sql scripts.

(images/Functions2.jpg)

## Then I run the function call in main.

images/Main3.jpg

##  Here is an example of a SQL Update call.
It changes the year from 1960 to 1961.

images/Update4.jpg

## Extra How to Install and Setup Projects

Create a new repo in Git Hub.  Make sure to include README when creating the new repo.

Clone the new repo to your machine.
```
git clone https://github.com/hrawp/datafun-05-sql
```

Add a .gitignore file with:
## Python virtual environment.
```
.venv/
```

## Visual Studio Code settings and workspace.
```
.vscode/
```
added so .venv files will not be sent up to your repo.

## Create a virtual environement by running this command.
```
python -m venv .venv
```

## Activate the environment by running this command.
```
.\.venv\Scripts\activate
```

## Update the requirements.txt with libraries that need to be installed.



## Run the three Git commands to stange and transmit files to GitHub.
```
git add .
```
```
git commit -m "initial commit"
```
```
git push origin main
```


## install depedencies from requirements.txt
```
py -m pip install -r requirements.txt
```