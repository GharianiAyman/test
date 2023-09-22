# Report for a homework test at Sens4Data.

## How to run the project 

* Get this project from Github

``` 
git clone https://github.com/GharianiAyman/test.git
 
```

* Install Postgres DB and configure a user and a DataBase

* Change the url line in ` database.py `

* Execute this command : 

``` 

python -m venv env 

``` 
* install requirements by executing this command : 

``` 
pip install -r requirement.txt

```
* Create a Task DB by executing this command : 

``` 
python3 createDB.py

```
* Execute unit test by executing this command (verify "id" on tests, you should execute current version with an empty DB) :

``` 
python3 test.py

```

* Run the project by executing this command : 

``` 
uvicorn main:app --reload

```