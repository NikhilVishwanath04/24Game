import itertools

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, lnode):
        """
        Assign left to left node
        """
        self.left = lnode
        
    def add_right(self, rnode):
        """
        Assign right to right node
        """
        self.right = rnode
        
    def evaluate(self):
        """
        Evaluate through operators, and assign left and right values based on 
        whether it is found in dictionary, else raise an error
        """
        if self.value in BETNode.CARD_VAL_DICT: # Base case: if value is a number, return value
            return BETNode.CARD_VAL_DICT[self.value]
        elif self.value in BETNode.OPERATORS: # If value is an operator, recurse through values for left & right and use operators respectively
            lval = self.left.evaluate()
            rval = self.right.evaluate()
            result = True 
            if lval and rval is not None: #To avoid None TypeError

                if self.value == "+":
                    return lval + rval
                elif self.value == "-":
                    return lval - rval
                elif self.value == "*":
                    return lval * rval
                elif self.value == "/":
                    try: # To avoid ZeroDivision Error
                        lval / rval
                    except: # Will not return division if false is the result (when rval is 0)
                        result = False 
                    if result == True: 
                        return lval / rval
    
    def __repr__(self, string=None):
        """
        Represent output as string value
        """
        if string == None:
            string = ''
        if self.value in BETNode.CARD_VAL_DICT:
            return string + str(self.value)
        elif self.value in BETNode.OPERATORS:
            lval = repr(self.left) # Recursive algorithm for display value
            rval = repr(self.right)

            if self.value == "+":
                return string + "(" + lval + "+" + rval + ")" #Uses proper formatting to display string repr
            elif self.value == "-":
                return string + "(" + lval + "-" + rval + ")"
            elif self.value == "*":
                return string + "(" + lval + "*" + rval + ")"
            elif self.value == "/":
                return string + "(" + lval + "/" + rval + ")"

def create_trees(cards):
    """
    Returns a set of all possible trees given 4 cards
    """
    trees = set() # Empty set to be added onto and returned
    ops = set(BETNode.OPERATORS) # Set of operators
    card_perm = set(itertools.permutations(cards)) # Develops all possible permutations for cards
    op_perm = set(itertools.product(ops, repeat=3)) # Develops all possible permutations for operations

    for card in card_perm:
        for operation in op_perm:

            #CCXCCXX
            root = BETNode(operation[2])
            root.add_right(BETNode(operation[1]))
            root.add_left(BETNode(operation[0]))
            root.right.add_right(BETNode(card[3]))
            root.right.add_left(BETNode(card[2]))
            root.left.add_right(BETNode(card[1]))
            root.left.add_left(BETNode(card[0]))
            trees.add(root)

            #CCXCXCX
            root = BETNode(operation[2])
            root.add_right(BETNode(card[3]))
            root.add_left(BETNode(operation[1]))
            root.left.add_right(BETNode(card[2]))
            root.left.add_left(BETNode(operation[0]))
            root.left.left.add_right(BETNode(card[1]))
            root.left.left.add_left(BETNode(card[0]))
            trees.add(root)

            #CCCXXCX
            root = BETNode(operation[2])
            root.add_right(BETNode(card[3]))
            root.add_left(BETNode(operation[1]))
            root.left.add_right(BETNode(operation[0]))
            root.left.add_left(BETNode(card[0]))
            root.left.right.add_right(BETNode(card[2]))
            root.left.right.add_left(BETNode(card[1]))
            trees.add(root)

            #CCCXCXX
            root = BETNode(operation[2])
            root.add_right(BETNode(operation[1]))
            root.add_left(BETNode(card[0]))
            root.right.add_right(BETNode(card[3]))
            root.right.add_left(BETNode(operation[0]))
            root.right.left.add_right(BETNode(card[2]))
            root.right.left.add_left(BETNode(card[1]))
            trees.add(root)

            #CCCCXXX
            root = BETNode(operation[2])
            root.add_right(BETNode(operation[1]))
            root.add_left(BETNode(card[0]))
            root.right.add_right(BETNode(operation[0]))
            root.right.add_left(BETNode(card[1]))
            root.right.right.add_right(BETNode(card[3]))
            root.right.right.add_left(BETNode(card[2]))
            trees.add(root)

    return trees

def find_solutions(cards):
    """
    Returns a set of solutions in string form
    """
    trees = create_trees(cards) 
    sols = set()
    for tree in trees: # Traverse through root of roots
                if tree.evaluate() == 24: # If root evaluation is equal to 24, add to set of solutions
                    sols.add(repr(tree))
    return sols