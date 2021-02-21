from lol.datatype.arrays import Array
from lol.database.database import Database

from lol.prompt import Prompt

def main():
    query = ["Org Name", "Members separated by spaces"]
    for element in query:
        prompt = Prompt(query)
    
    members = Array.create(str(members).split(" "))

if __name__ == "__main__":
    main()