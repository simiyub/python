
class Node:
    def __init__(self, value):
        self.children = []
        self.value = value
        self.next = None
        self.previous = None

    def addChild(self, name):
        self.children.append(Node(name))
        return self