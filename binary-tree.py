
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
        
    def preorder_search(self, start, find_val):
        if start != None and start.value == find_val:
            return True
        elif start.left != None:
            return self.preorder_search(start.left, find_val)
        elif start.right != None:
            return self.preorder_search(start.right, find_val)
        else:
            return False

    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Tests
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.search(4))
print(tree.search(6))
print(tree.print_tree())