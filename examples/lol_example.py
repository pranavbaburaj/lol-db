from lol.datatype.arrays import Array
from lol.database.database import Database

from lol.prompt import Prompt

org = Database("name", "members")


def main():
    query = ["Org Name", "Members separated by spaces"]
    sol = {}
    for element in query:
        prompt = Prompt(query)
        sol[element] = prompt.prompt()
    
    members = Array.create(str(sol["Members separated by spaces"]).split(" "))

    org.add([sol["Org Name"], members)

if __name__ == "__main__":
    main()