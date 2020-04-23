import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call 'insert' on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            else:
                # the left side is empty
                # we've found parking spot
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value
        else: # value is greater than or equal to
            if self.right:
                self.right.insert(value)
            else:
                # the right side is empty
                # we've found parking spot
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case: if value is target, return True
        if self.value == target:
            return True
        # if target is less than node, go left
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                # if get to the end, does not contain target
                return False
        else:
            # if target is larger than node, go right
            if self.right:
                return self.right.contains(target)
            else:
                # if get to the end on right, does not contain target
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # will be furthest node to right.
        # base case: no nodes to right.
        if self.right is None:
            return self.value
        else:
            # if can go right, go furthest to right.
            if self.right:
                return self.right.get_max()



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
