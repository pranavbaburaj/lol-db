# Database
<hr>

## How to get started with lol database?
```python
# importing the database
from lol.database.database import Database

# create the database class 
# by pasing in the table name
# and the fiedls in the database
database = Database("table_name", ["name", "age"])
```
<hr>

> By default the database will create a  log message
everytime you perform an action . To stop this
call the set_track_modification function

```python
database.set_track_modification(False)
```
<hr>

Add an item to the database
```python
# Pass in the data required as the parameters
database.add(["Pranav Baburaj", 13])
```
Delete an item from the database
```python
# pass in the object id as the parameter
database.delete(object_id)
```
Change a field from database
```python
# pass in the object_id, the key and the new 
# data as the parameters
database.change(object_id, "name", "lol")
```
Filter out elements from the database
```python
database.filter({name:"Pranav"})

# returns you the object id 
```
Get the information from the database
```python
# pass in the object id
database.get(object_id)
```

#### Other methods
Get all the object ids
```python
database.ids()
```
Clear the database
```python
database.clear()
```

