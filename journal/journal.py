import os
from journal import entry

class Journal:

    def __init__(self, name):
        self.name = name
        self.entries = {}
        os.makedirs(os.path.join(".", "journal", "journals", self.name))


    def list_entries(self):
        for x in self.entries:
            print(x)


    def edit(self, name):
        self.entries[name].open()


    def add(self, name):
        if name in self.entries:
            print("Error: Name already exists")
            return
        self.entries[name] = entry(name, "./journal/journals/" + self.name + "/" + name)
