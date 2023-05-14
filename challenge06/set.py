#!/usr/bin/env python3
'''
Title:      set.py
Abstract:   Implement a set using a linked-based binary tree.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   2 hours
Date:       3/30/23

Questions:
    1. While performing a DFS, how do you know if node is valid or not?
        It has to satisfy the constraints of the problem and not already been visited. 
        Usually, you use a data structure like a set to keep track of visited nodes so 
        you don't visit them again, preventing inifnite loops and not necessary traversals.
    2. What is the worst-case time complexity of Set.search()?
        O(h) where h is the height of the binary search tree where you traverse from the root node 
        to the deepest leaf node (taking h steps).
    3. What is the worst-case space complexity of Set.search()?
       It would be O(1) if I wasn't using additional space like creating new data structures or allocating 
        memory for new variables; however, there is an implicit space overhead associated with the call stack 
        due to recursion, so the worst-case is actually O(h). 
'''
from dataclasses import dataclass
# Classes
@dataclass
class Node:
    value: int
    left: 'Node' = None
    right: 'Node' = None
class Set:
    ''' Simple set using a linked-based binary tree. '''
    def __init__(self, root):
        ''' Initialize internal binary tree. 
        >>> s = Set(Node(4, Node(6, Node(3), Node(7)), Node(6))); s.root
        Node(value=4, left=Node(value=6, left=Node(value=3, left=None, right=None), right=Node(value=7, left=None, right=None)), right=Node(value=6, left=None, right=None))
        '''
        self.root = root
    def search(self, value):
        ''' Return whether or not value is contained within the set.
        Call the recursive method on the tree's root and return the result.
        '''
        return self._search(self.root, value)
    def _search(self, node, value):
        ''' Return whether or not value is contained within the set.
        Walk tree using DFS to find value and return True if found (otherwise
        False).
        >>> s = Set(Node(4, Node(6, Node(3), Node(7)), Node(6)))
        >>> all(s.search(n) for n in [3, 4, 6, 7])
        True
        
        >>> any(s.search(n) for n in [0, 1, 2, 5, 9])
        False
        '''
        if node is None:
            return False
        if node.value == value:
            return True
        return self._search(node.left, value) or self._search(node.right, value)
