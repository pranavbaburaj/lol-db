from lol.database.database import Database


data = Database("hello world", ["name", "age"])

d = True
while d:
	f = str(input(">>>>"))
	if f == "!":
		d = False
	else:
		data.add([f, len(f)])