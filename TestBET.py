import unittest
from BET import BETNode, create_trees, find_solutions

class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        r"""
        Tree with string repr
               *
              / \
             +   2
            / \
           -   3
          / \
         9   3
        """
        root = BETNode('*')
        root.add_left(BETNode("+"))
        root.add_right(BETNode("2"))
        root.left.add_left(BETNode("-"))
        root.left.add_right(BETNode("3"))
        root.left.left.add_left(BETNode("9"))
        root.left.left.add_right(BETNode("3"))
        self.assertEqual(root.evaluate(), 18)

    def test_evaluate_tree2(self):
        r"""
        Tree with string repr
                /
              /  \
             *    +
            / \  / \
           6  3  A  8
        """
        root = BETNode('/')
        root.add_left(BETNode("*"))
        root.add_right(BETNode("+"))
        root.right.add_left(BETNode("A"))
        root.right.add_right(BETNode("8"))
        root.left.add_left(BETNode("3"))
        root.left.add_right(BETNode("6"))
        self.assertEqual(root.evaluate(), 2)

class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        """
        Tests hand with 7680 possible valid trees (4 unique cards)
        """
        cards = ["A", "4", "Q", "K"]
        self.assertEqual(len(create_trees(cards)), 7680)

    def test_hand2(self):
        """
        Tests hand with 3840 possible valid trees (1 duplicate set of cards)
        """
        cards = ["A", "A", "Q", "K"]
        self.assertEqual(len(create_trees(cards)), 3840)

class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        """
        Tests hand with 0 solutions, returns empty set
        """
        cards = ["A", "A", "A", "A"]
        self.assertEqual(len(find_solutions(cards)), 0)
        self.assertEqual(find_solutions(cards), set())

    def test_A23Q(self): 
        """
        Tests hand A23Q with 33 solutions, returns set of solutions in string form
        """
        cards = ["A", "2", "3", "Q"]
        self.assertEqual(len(find_solutions(cards)), 33)
        self.assertEqual(find_solutions(cards), {'((A+(3-2))*Q)', '((A+3)*(Q/2))', '(((A-2)+3)*Q)', '((3+A)/(2/Q))', '((Q*(A+3))/2)', '(Q*(A-(2-3)))', 
                                                 '(((3+A)-2)*Q)', '((3+A)*(Q/2))', '((3+(A-2))*Q)', '(((3+A)/2)*Q)', '(Q*((A+3)/2))', '(Q*((A+3)-2))', 
                                                 '((A+3)/(2/Q))', '(((A+3)*Q)/2)', '(Q*((3+A)/2))', '((Q/2)*(A+3))', '(Q*(A+(3-2)))', '(Q*((3-2)+A))', 
                                                 '(Q*(3-(2-A)))', '(((A+3)-2)*Q)', '(Q/((3/2)-A))', '(((3-2)+A)*Q)', '(Q/(2/(A+3)))', '(((3+A)*Q)/2)', 
                                                 '(Q*((A-2)+3))', '((A-(2-3))*Q)', '(Q/(2/(3+A)))', '((Q*(3+A))/2)', '(Q*(3+(A-2)))', '((Q/2)*(3+A))',
                                                 '(((A+3)/2)*Q)', '((3-(2-A))*Q)', '(Q*((3+A)-2))'})
        
unittest.main()