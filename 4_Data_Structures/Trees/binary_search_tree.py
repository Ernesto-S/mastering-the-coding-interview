# create a class for a binary search tree
# the goal is to create this tree
#      9
#    /   \
#   4     20
#  / \   /  \
# 1   6 15  170


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

        

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        # insert value into binary search tree
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = newNode
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = newNode
                        break
                    else:
                        current = current.right
                else:
                    # Value already exists in the tree, do not insert duplicates
                    return self

    def lookup(self,value):
        # look up a value
        current = self.root
        while current is not None:
            if current.value == value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    # def delete(self,node,value):
    #     # delete a value from the tree
    #     if node is None:
    #         return node
    #     if value < node.value:
    #         node.left = self.delete(node.left, value)
    #     elif value > node.value:
    #         node.right = self.delete(node.right, value)
    #     else:
    #         # Node with only one child or no child
    #         if node.left is None:
    #             return node.right
    #         elif node.right is None:
    #             return node.left
    #         # Node with two children: Get the inorder successor (smallest in the right subtree)
    #         min_larger_node = self._find_min(node.right)
    #         node.value = min_larger_node.value
    #         node.right = self.delete(node.right, min_larger_node.value)
    #     return node

    def __str__(self):
        values = []
        self._in_order_traversal(self.root, values)
        return " ".join(str(v) for v in values)

    def _in_order_traversal(self, node, values):
        if node is not None:
            self._in_order_traversal(node.left, values)
            values.append(node.value)
            self._in_order_traversal(node.right, values)



tree = Binary_Search_Tree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree)  # Should print the values in sorted order: 1 4 6 9 15 20 170
print(tree.lookup(15).value)  # Should print 15

    

    