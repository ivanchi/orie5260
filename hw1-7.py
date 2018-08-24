class Tree(object):

    def __init__(self, root):
        """Initialize the root
        """
        self.root = root

    def get_value_root(self):
        """Get the root value of the tree
        """
        if self.root is not None:
            return self.root.value
        else:
            return None


    def printTree(self):
        """Get the list of the list for a tree
        """
        h = self.getDepth(self.root)
        #the maximum code for depth of h
        r = 2**h - 1
        #Initialize the list of list using maximum number of node
        lst = [["|" for i in range(r)] for j in range(h)]
        lst = self.getAns(self.root, lst, h - 1, 2**(h - 1) - 1)
        for col in lst:
            for e in col:
                print(e, end="")
            print()


    def getAns(self, root, lst, level, pos):
        """Modify "|" in the list of list to the value of the node.
        """
        #Change to the value of a node starting from the 1st level
        if isinstance(root, Node):
            lst[-level - 1][pos] = str(root.value)
            #Go to the next level and adjust the position based on if it is on
            #the left or right
            if root.left or root.left == 0:
                self.getAns(root.left, lst, level - 1, pos - 2 ** (level - 1))
            if root.right or root.right == 0: 
                self.getAns(root.right, lst, level - 1, pos + 2 ** (level - 1))
        else:
            lst[-level - 1][pos] = str(root)
        return lst


    def getDepth(self, root):
        #Recursively calculate the depth of the tree
        if root is not None and isinstance(root, Node):
            return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
        else:
            return 1




class Node(object):

    def __init__(self, value, left, right):
        #Initialize the node
        self.value = value
        self.left = left
        self.right = right

if __name__ == '__main__':
    a = Node(1, Node(2, 4, None), 3)
    b = Tree(a)
    b.printTree()
