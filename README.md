


# datafun-05-sql
'''
SQL work with Python  
'''
'''
In this project I use Python to call SQL scripts.  To start off with, I load two csv tables, books and authors, with data into project.db. I then follow the steps below to interact with the data to perform sql commands.
'''
## I run db_initialize_aaron.py 
'''
This sets up the database and pulls in data from two csv files authors and books.
'''
## Next I run db_operations_aaron.py
'''
This has what imports we need at the top.
'''
## I define logging then setup all the diffrent file paths to the .sql files.

[Define](Define1.JPG)

## Then I define the functions which call the .sql scripts.

[Functions](Functions2.JPG)

## Then I run the function call in main.

[Main](Main3.JPG)

##  Here is an example of a SQL Update call.
'''
It changes the year from 1960 to 1961.
'''

[Update](Update4.JPG)

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