from lol.argparse import Parser
import sys

def get(data):
    print(data)

p = Parser([
    {
        "value" : "install $package",
        "types" : {
            "package" : str
        },
        "func" : get
    }
])

# from lol.prompt import Prompt

# p = Prompt("Name", verify="email", typeof=str)

# # p.error("hello")

# d = p.option([
#     {"prompt" : "Hai", "selector" : 1},
#     {"prompt" : "Hello", "selector" : 2},
#     {"prompt" : "Hoo", "selector" : 3}
# ])

# print(d)
# from lol.prompt import Prompt

# p = Prompt("Name", verify="email", typeof=str)

# # from lol.switch import switch

# # def data():
# #     print("lol")

# # d = switch(
# #     5, {
# #         8 : data,
# #         6 : data,
# #         58 : data,
# #         None : data
# #     }
# # )

# # d()

# # from lol.datatypes.maps import Maps

# # mapobj = Maps.create({
# #     "name" : 9,
# #     "name" : 9938,
# #     "age" : 9,

# #     "class" : 8,
# #     "age" : 00,
# #     "house" :999,
# #     "class" : 99999
# # })

# # print(mapobj.get())

# # from lol.datatypes.array import Array

# # data = Array.create({"name" : ["hello"], 4 : ["d"]})

# # print(data.get())

# # from lol.datatypes.interface import Interface

# # data = Interface({"name":[str], "age" : [int]})
# # o = data.create("Pranav", 13)

# # print(o.get_item("name"))

# # o.set_item("name", "99")
# # print(o.get_item("name"))

# # from lol.database.database import Database
# # from lol.database.serializer import DatabaseSerializer

# # d = Database("hello world", ["name", "age"])

# # d.add(["Hai", 885885])

# # f = DatabaseSerializer(d)

# # print(f.xml())
# # d.set_track_modification(False)
# # d.add([5, 7])

# # l = d.ids()[0]
# # d.change(l, "age", 8183912893812)
# # d.delete("d.ids()[0]")

# # from lol.datatypes.number import Number

# # d = Number(4234.)

# # print(d.set_(66))
# # print(d.get())


# # print(d.get())
# # from lol.datatypes.interface import Interface

# # d = Interface({"data" : [str]})

# # l = d.create("Hai")

# # print(l.get_item("data"))
# # from lol.datatypes.string import String

# # f = String(" qewd qec cwefcw")

# # print(f.length())

# # # print(f.has("7"))
# # print(f.character_at(3))

# # print(f.remove_spaces())
# # from lol.database.database import LOL as Table
# # import lol.datatypes.array as data

# # m = data.LOLArray(int)
# # m.add(5443543)
# # m.add(423424)
# # m.add(824898234)
# # m.add(898498239842)

# # print(m.range("max"))

# # m = data.Maps((int, int))

# # m.add(6, 7)

# # m.add(8, 8)
# # m.add(5, 7)

# # m.change(5, 33423424)
# # print(m.get())

# # d = Table("hello", ["data", "bata"])

# # f = data.LOLArray(int, None)


# # print(f.all())

# # f.add(6)

# # f.add(64)

# # f.add(6)

# # f.add(64)
# # f.add(8)
# # f.add(7)

# # # print(f.element_at(0))

# # # print(f.find
# # print(f.choice())



