import unittest
from tree.tree import Tree, Node


class testTree(unittest.TestCase):

    def test_tree1(self):
        node = Node(5, None, None)
        tree = Tree(node)
        assert tree.printTree() == [["5"]]

    def test_tree2(self):
        node = Node(3, Node(9, 22, 105), Node(554, 10, 0))
        tree = Tree(node)
        assert tree.printTree() == [["|", "|", "|", "3", "|", "|", "|"],
                                    ["|", "9", "|", "|", "|", "554", "|"],
                                    ["22", "|", "105", "|", "10", "|", "0"]]

    def test_tree3(self):
        node = Node(10, Node(5, Node(55, Node(99, None, None), None), None), None)
        tree = Tree(node)
        assert tree.printTree() == [["|", "|", "|", "|", "|", "|", "|",
                                     "10", "|", "|", "|", "|", "|", "|", "|"],
                                    ["|", "|", "|", "5", "|", "|", "|", "|",
                                     "|", "|", "|", "|", "|", "|", "|"],
                                    ["|", "55", "|", "|", "|", "|", "|", "|",
                                     "|", "|", "|", "|", "|", "|", "|"],
                                    ["99", "|", "|", "|", "|", "|", "|",
                                     "|", "|", "|", "|", "|", "|", "|", "|"]]

    def test_tree4(self):
        node = Node(8, Node(3, None, 14), Node(50, Node(22, None, 200), None))
        tree = Tree(node)
        assert tree.printTree() == [["|", "|", "|", "|", "|", "|", "|", "8",
                                     "|", "|", "|", "|", "|", "|", "|"],
                                    ["|", "|", "|", "3", "|", "|", "|", "|",
                                     "|", "|", "|", "50", "|", "|", "|"],
                                    ["|", "|", "|", "|", "|", "14", "|", "|",
                                     "|", "22", "|", "|", "|", "|", "|"],
                                    ["|", "|", "|", "|", "|", "|", "|", "|",
                                     "|", "|", "200", "|", "|", "|", "|"]]
