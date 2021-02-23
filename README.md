# LOL
Lol is a database library
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
- Prompt
    - Input prompt
    - Options(coming soon)
- Project generator

## How to use it
### Database
See the database documentation [here](https://github.com/pranavbaburaj/lol/blob/master/docs/database.md)

<hr>

### Datatypes

See all the datatype methods [here](https://github.com/pranavbaburaj/lol/blob/master/docs/types.md)
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
print(obj.get_item('name'))

# change the value
obj.set_item('name', 'new-name')
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

### CLI

#### Project Generator
```
lol-create-project
```


### Prompts and options
```python
from lol.prompt import Prompt

data = Prompt("Name", type=str).prompt()
```

<<<<<<< HEAD
```python
from lol.argparse import Parser
import sys

def get(data):
    print(data)

def delete(data):
    print(data)

p = Parser([
    {
        "value" : "install $package",
        "types" : {
            "package" : str
        },
        "func" : get
    },
    {
        "value" : "delete $package",
        "types" : {
            "package" : str
        },
        "func" : delete
    }
])

p.parse()
```

=======
### ArgParser
> Under development
>>>>>>> 21da2c171f7b29ae400e1cdf9ff786edb9279b8b
