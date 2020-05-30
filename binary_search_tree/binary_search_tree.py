"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('../stack')
from stack import Stack
from q import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
            # Recursive
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

                
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        curr_max = self.value
        if self.right is None:
            return curr_max
        else:
            return self.right.get_max()
        
        # curr_max = self
        # while curr_max.right:
        #     curr_max = curr_max.right
        # return curr_max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        
        print(node.value)
        
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make a queue
        queue = Queue()
        # add node to queue
        queue.enqueue(node)
        # while the queue is not empty
        while len(queue) > 0:
        # remove node from queue
            curr_node = queue.dequeue()
        # print(queue.value)
            print(curr_node.value, 'current node')
            
        # get left child of current node
            if curr_node.left:
                queue.enqueue(curr_node.left)

        # get right child of current node
            if curr_node.right:
                queue.enqueue(curr_node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make a stack
        stack = Stack()
        # push the node on the stack
        stack.push(node)
        # while the stack is not empty
        while len(stack) > 0:
        # pop of the top of the stack
            curr_node = stack.pop()
            print(curr_node.value, 'stack')
        # put the kids of the current node on the stack
            if curr_node.right:
                stack.push(curr_node.right)
            
            
            if curr_node.left:
                stack.push(curr_node.left)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
bst.insert(4)
bst.insert(9)
bst.insert(2)
bst.insert(10)
bst.dft_print(bst)
bst.bft_print(bst)
