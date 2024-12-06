# In this practice, you will use classes to implement a binary search
# tree and perform pre-order, in-order, and post-order traversal of
# the tree.

# Implement a class Node with a constructor method that defines the
# following instance properties: - The lefthand child of the node,
# initialized to None - The righthand child of the node, initialized
# to None - The value of the node, initialized to the value passed
# into the constructor

# Implement another class Tree with the following instance methods:

# - insert() that takes in the root node and a new node and places the
#   new node in the correct location in the binary search tree

# - preorder_traversal() that traverses the tree and prints the value
#   of each node in pre-order succession

# - inorder_traversal() that traverses the tree and prints the value
#   of each node in in-order succession

# - postorder_traversal() that traverses the tree and prints the value
#   of each node in post-order succession


# Write your class here.
class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node({self.value}, {self.left}, {self.right})"


class Tree:
    def insert(self, root, node):
        if root.value < node.value:
            if root.right:
                self.insert(root.right, node)
            else:
                root.right = node
        elif node.value < root.value:
            if root.left:
                self.insert(root.left, node)
            else:
                root.left = node

    def preorder_traversal(self, root):
        if not root:
            return
        print(root.value)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        print(root.value)
        self.inorder_traversal(root.right)

    def postorder_traversal(self, root):
        if not root:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.value)


tree = Tree()

root = Node(4)
tree.insert(root, Node(1))
tree.insert(root, Node(2))
tree.insert(root, Node(3))

print(f"{root = }")

print("** PRE ORDER: **")
tree.preorder_traversal(root)  # 4, 1, 2, 3

print("** IN ORDER: **")
tree.inorder_traversal(root)  # 1, 2, 3, 4

print("** POST ORDER: **")
tree.postorder_traversal(root)  # 3, 2, 1, 4
