# LOL
Lol is a database library(An improved version of [json-based-database](https://github.com/pranavbaburaj/json-based-database))
<hr>

# Features
- A set of data types
    - Numbers
    - Strings
    - Maps
    - Arrays
    - Interfaces
- A json-based-database
    - Add
    - Delete
    - Update
    - Filter

## How to use it
### Database
See the database documentation [here](https://github.com/pranavbaburaj/lol/blob/master/docs/database.md)

<hr>

### Datatypes

See all the datatype methods [here](https://github.com/pranavbaburaj/lol/blob/master/docs/types.md)
#### Arrays
```python
from loldb.datatypes.arrays import Array

array = Array(int, length=None)
```
#### Maps
```python
from loldb.datatypes.maps import Maps

maps = Maps((int, str))
```

#### Interfaces
```python
from loldb.datatypes.interface import Interface

data = Interface({
    name : [str, int],
    age : "?" # any,
})

# create an interface object
obj = data.create("Pranav", 13)

# gives you the name
print(obj.get('name'))
```

#### Numbers
```python
from loldb.datatypes.number import Number

num = Number("777")

```

#### Strings
```python
from loldb.datatypes.string import String

string = String(7777)
```