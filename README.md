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
Under construction

<hr>

### Datatypes
#### Arrays
```python
from lol.datatypes.arrays import Array

array = Array(int, length=None)
```
#### Maps
```python
from lol.datatypes.maps import Maps

maps = Maps((int, str))
```

#### Interfaces
```python
from lol.datatypes.interface import Interface

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
from lol.datatypes.number import Number

num = Number("777")

```

#### Strings
```python
from lol.datatypes.string import String

string = String(7777)
```