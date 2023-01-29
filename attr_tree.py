class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_index(self):
        count = 0
        for i in self.parent.children:
            if self == i:
                return count
            count += 1


class Tree:
    def __init__(self, policy):
        self.root = Node(policy[0])

    def get_node(self, i):
        for n in self.root.children:
            if n == i:
                return n

    def build(self, policy):
        for i in range(1, len(policy)):
            child = Node(policy[i])
            if child.data == "AND" or child.data == "OR":
                self.root.add_child(child)
                child.parent = self.root
                self.root = child
            elif child.data == "/" and self.root.parent is not None:
                self.root = self.root.parent
            else:
                self.root.add_child(child)
                child.parent = self.root

    def access(self, attr):
        count = 0
        if self.root.data == "AND":
            k = len(self.root.children)
            for i in self.root.children:
                self.root = i
                count += self.access(attr)
            if count >= k:
                return 1
            else:
                return 0

        elif self.root.data == "OR":
            for i in self.root.children:
                self.root = i
                count += self.access(attr)
            if count >= 1:
                return 1
            else:
                return 0
        else:
            return self.evaluate(attr)

    def evaluate(self, attr):
        if self.root.data in attr:
            return 1
        else:
            return 0


def results(i):
    if i == 1:
        print("access granted")
    else:
        print("access denied")


pol = ["OR", "DOCTOR", "AND", "NURSE", "HOSPITAL", "/"]

attr1 = ["HOSPITAL", "DOCTOR"]
attr2 = ["NURSE"]
attr3 = ["HOSPITAL", "NURSE"]

tree = Tree(pol)
tree.build(pol)

results(tree.access(attr1))
results(tree.access(attr2))
results(tree.access(attr3))
