from Node import Node

class Network:
    def __init__(self):
        self.network = dict()
        self.name = str

    def setName(self, name):
        self.name = name

    def addNode(self, node: Node):
        self.network[node.name] = node

    def getNode(self, name) -> Node:
        return self.network[name]

    def getVariables(self) -> list:
        return list(self.network.keys())