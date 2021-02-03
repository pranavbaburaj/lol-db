from lol.database.database import LOL as Table
import lol.datatypes.array as data
# d = Table("hello", ["data", "bata"])

f = data.LOLArray(int, 2)


print(f.all())

f.add(6)

f.add(64)

f.add(644)

f.add(64)

print(f.all())
