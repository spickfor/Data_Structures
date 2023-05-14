#!/usr/bin/env python3


#  Title: set.py
#  Abstract: implement set using binary search tree
#  Author: Seth Pickford
#  Email: spickfor@nd.edu
#  Estimate: 1 hrs
#  Date: 3/29/23


'''
Questions:
    1. What is the average time complexity insert()?
        O(log n)
    The average time complexity of insert() is O(log n), where n is the number of elements in the tree. This is because, on average, the tree height grows logarithmically with the number of elements.
    
    2. What is the worst-case time complexity insert()?
        O(n)
        The worst-case time complexity of insert() is O(n), where n is the number of elements in the tree. This happens when the tree is degenerate (i.e., all nodes are in a single line) and the new node is inserted at the end of the line. In this case, we need to traverse all n nodes to find the correct location for the new node.
    
    3. What is the base case for the _insert() and _search() methods?
        The base case for both is when the node is None.
        The base case for the _insert() and _search() methods is when the current node is None, indicating that we have reached the end of a branch in the tree and have not found the value we are looking for (in the case of search()) or the location where the new node should be inserted (in the case of insert()).
'''

import set

class Node:
    ''' Simple Node with value and left and right children. '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node({self.value})'

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.value == other.value and self.left == other.left and self.right == other.right

class Set:
    ''' Simple Set Implementation based on a binary search tree. '''
    def __init__(self):
        ''' Initialize empty set.
        >>> s = Set(); not s.root
        True
        '''
        self.root = None

    def insert(self, value):
        ''' Insert value into set.
        Test tree:
                 5
               /   \
              4     7
             /       \
            1         9
        >>> s = Set()
        >>> s.insert(5); s.root.value
        5
        >>> s.insert(7); s.root.right.value
        7
        >>> s.insert(4); s.root.left.value
        4
        >>> s.insert(9); s.root.right.right.value
        9
        >>> s.insert(1); s.root.left.left.value
        1
        '''
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        ''' Insert value into set (recursive). '''
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)
        # else value is already in the set, do nothing

    def search(self, value):
        ''' Return whether or not value is in set.
        >>> s = Set()
        >>> for n in [5, 7, 4, 9, 1]: s.insert(n)
        >>> all(s.search(n) for n in [5, 7, 4, 9, 1])
        True
        >>> any(s.search(n) for n in [0, 3, 8, 10])
        False
        '''
        return self._search(self.root, value)
    
    def _search(self, node, value):
        ''' Return whether or not value is in set (recursive). '''
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
