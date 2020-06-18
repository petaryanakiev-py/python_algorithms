
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None

class BinarySearchTree(object):
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, new_value):
        self.insert_at(self.root, new_value)

    def insert_at(self, node, new_value):
        if new_value > node.value:
            if node.right:
                self.insert_at(node.right, new_value)
            else:
                node.right = Node(new_value)
        else:
            if node.left:
                self.insert_at(node.left, new_value)
            else:
                node.left = Node(new_value)

    def search(self, value_to_search):
        return self.search_at(self.root, value_to_search)

    def search_at(self, node, value_to_search):
        if node:
            if value_to_search == node.value:
                return True
            elif value_to_search < node.value:
                return self.search_at(node.left, value_to_search)
            else:
                return self.search_at(node.right, value_to_search)
        return False

    def print_tree(self):
        self.print_tree_inorder(self.root)

    def print_tree_inorder(self, node):
        if node != None:
            self.print_tree_inorder(node.left)
            print(node.value)
            self.print_tree_inorder(node.right)

# Tests
bst = BinarySearchTree(4) # Binary Search Tree with root 4
bst.insert(9)
bst.insert(1)
bst.insert(12)

print(bst.search(8))
print(bst.search(12))

bst.print_tree()