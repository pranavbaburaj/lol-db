## Types available in LOL

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
