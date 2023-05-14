#!/usr/bin/env python3

'''
Title:      tree.py
Abstract:   Implement a binary tree read and walk functions.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hour
Date:       4/4/2023
Questions:
    1. What is the worst-case time complexity of tree_read()?
        O(n)
    2. What is the worst-case time complexity of tree_walk()?
        O(n)
    3. In tree_walk(), how did you modify BFS to print all the nodes on one
    comma-separated line?
        Stored node values in a list and used str.join to print them.
    4. In tree_walk(), how did you remove any trailing invalid nodes from your
    output?
        Added a condition to check for valid nodes before appending their values.
'''

from collections import deque

# Classes

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(value={self.value}, left={self.left}, right={self.right})"

# Functions

def tree_read(array, index=0):
    '''
    Return a node-based tree from the given array of values in BFS format.
    >>> tree_read([1, 2, 3])
    Node(value=1, left=Node(value=2, left=None, right=None), right=Node(value=3, left=None, right=None))
    >>> tree_read([1, 2, 3, 4, 0, 0, 6])
    Node(value=1, left=Node(value=2, left=Node(value=4, left=None, right=None), right=None), right=Node(value=3, left=None, right=Node(value=6, left=None, right=None)))
    '''
    if index >= len(array) or array[index] == 0:
        return None

    node = Node(value=array[index])
    node.left = tree_read(array, 2 * index + 1)
    node.right = tree_read(array, 2 * index + 2)

    return node

def tree_walk(root):
    '''
    Print out the tree in level-by-level order with each level on the same
    line.
    >>> tree_walk(tree_read([1, 2, 3]))
    1, 2, 3
    >>> tree_walk(tree_read([1, 2, 3, 4, 0, 0, 6]))
    1, 2, 3, 4, 6
    '''
    if not root:
        return

    queue = deque([root])
    node_values = []

    while queue:
        node = queue.popleft()
        if node:
            node_values.append(str(node.value))
            if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)

    print(', '.join(node_values))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

