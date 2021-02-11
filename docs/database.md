In this tutorial, we will check out a database library in python, called [lol-db](https://github.com/pranavbaburaj/lol). Before starting this tutorial, I assume that you have a basic knowledge of python and pip. In this tutorial, we will be covering:

 - Setting up the project
 - Creating a database model
 - Other database methods

So, let's get started

# Project Setup
First of all, we have to set up a python project.

 - Create a virtual environment and activate it
	  Create a virtual environment 
	 `virtualenv env`
	 Activate the virtual environment
	 `source env/bin/activate`

- Install lol-db 
	Install lol-db using pip
	`pip install loldb`
- Create a python file
`touch main.py`

# Introducing lol-DB
lol-DB is a python utility library that mainly contains a database and several data types. In this tutorial, we will be going through the database

To use the lol-DB module, you will have to import it into your python file
```python
from lol.database import database, serializer
```
The lol database has two main parts:
 - The database
 - The serializer
 
 
 To create a new database model, you can add this code to your file
 ```python
 from lol.database import database
 
 # Create a model
 data = database.Database("database name", ["name", "age"])
 ```
 The `Database` class takes two main arguments,
 the name of the database(`str`) and an array of fields(`list of str`).


> By default the database will create a log message every time you perform an action. To stop this, add the following lines to your code 
> ```python
# set track modifications
data.set_track_modification(False)
> ```

### Add an item to the database
```python
data.add(["Pranav Baburaj", 13])
```
 
 The `database.add()` function takes one argument
 which is the list of fields

### Delete an item from the database
```python
# to get keys from the database
keys = data.ids()

# delete the last item from the database
data.delete(keys[-1])
```
The `delete` function takes a single argument which is the id of the item. You can obtain all the keys by adding this to your code
```python
data.ids()
```

### Change an item from the database
```python
data.change(
	data.ids()[-1], # the object id
	"name", # the field name,
	"P Pranav Baburaj" # the new value
)

```
### Filter out elements from the database
```python
database.filter(
	{
		"age" : 13
	}
)

# returns you the object id 
```
The `filter` function takes a single argument, which is a dict of items to match with the database fields. The function will return a list of object ids

### Get information from the database
```python
# pass in the object id
database.get(object_id)
```

### Clear the database
```python
database.clear()

```
<hr>

## Serializers

If you are using this module along with a web framework, you may have to convert the model into either JSON format or XML. To do this you can use the `database.serializer` module
```python
from lol.database import database, serialize

data = database.Database("database name", ["name", "age"])

# converting to json
print(data.jsonify())

# converting to XML
print(data.xml())
```

I hope you were able to learn something new from this blog, 

Star this repository on [GitHub](https://github.com/pranavbaburaj/lol)
 
