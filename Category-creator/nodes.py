

class Node:
    def __init__(self, _id, _name, _type, _parent):
        self.id = _id
        self.name = _name
        self.type = _type
        self.parent = _parent

    def __str__(self):
        return f"{self.id} {self.name} {self.type} {self.parent}"
