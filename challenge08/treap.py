#!/usr/bin/env python3
'''
Title:      treap.py
Abstract:   Implement a Map class using a treap.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hour
Date:       04/14/2023
Questions:
    1. What is worst-case time complexity of Map.insert()?
        In the worst case where the map's tree is sorted in the order of a linked list, the time complexity is O(n)
    2. What is worst-case time complexity of Map.search()?
        Worst case will be O(n)
    3. What role does a Node's priority play during insertion?
        A Node's priority plays a role in balancing the tree during insertions. Depending on the priority of the inserted
        node, the tree is rotated to be a max-heap for priority and better balance the tree
    4. How did you use a dictionary in Map._dump_tree() to help you print each
    level on a single line?
        The dictionary I used in the dump_tree() method serves to seperate the levels of the tree when searching BFS
        The number of possible nodes on each level is equal to 2 to the power of the level.  The keys of the dictionary
        represent the levels of the tree, and by calculating when the level is full, the nodes being queued for printing
        are put onto the next level.  This method also requires edgecases for trees in linked list format and those without
        children. Once the tree has been searched, I simpoly print each value of the dictionary as its own line.
'''


from collections import deque, defaultdict
from dataclasses import dataclass
from random      import random
# Classes
@dataclass
class Node:
    ''' Node with string key, int value, float priority, and left and right children. '''
    pass
    key: str
    value: int = None
    priority: float = None
    left: 'Node' = None
    right: 'Node' = None
class Map:
    ''' Map Implementation based on a treap. '''
    def __init__(self):
        ''' Initialize empty Map.
        >>> m = Map(); not m.root
        True
        '''
        pass
        #empty map with empty root
        self.root = None
    def insert(self, key, value, priority=None):
        ''' Insert key, value pair into Map.  If key is already in Map, then
        update value.
        >>> m = Map()
        >>> m.insert('D', 0, 60); m.root
        Node(key='D', value=0, priority=60, left=None, right=None)
        >>> m.insert('F', 1, 76); m.root.key        # Rotate Left
        'F'
        >>> m.insert('H', 2, 14); m.root.right.key
        'H'
        >>> m.insert('C', 3, 70); m.root.left.key   # Rotate Right
        'C'
        >>> m.insert('A', 4, 55); m.root.left.left.key
        'A'
        '''
        pass
        #Set tree's root to updated tree root after insertion
        self.root = self._insert(self.root, key, value, priority)
    def _insert(self, node, key, value, priority=None):
        ''' Recursively insert key, value pair into Map. '''
        pass
        #base case, insert node and recurse back up if node is empty
        if not node: return Node(key, value, priority or random())
        
        #if node with same key found, update value and return
        if node.key == key:
            node.value += value
            return node
        #BST invariant to search further left
        if key < node.key:
            node.left = self._insert(node.left, key, value, priority)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        #BST invariant to search further right
        if key > node.key:
            node.right = self._insert(node.right, key, value, priority)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        #Return node on way back up from recursion
        return node
    def lookup(self, key):
        ''' Lookup key in Map and return associated value (None if missing).
        >>> m = Map()
        >>> d = [('sbn', '574'), ('eau', '715'), ('sna', 714), ('nyc', 646)]
        >>> for k, v in d: m.insert(k, v)
        >>> all(m.lookup(k) == v for k, v in d)
        True
        >>> m.lookup('stl')
        '''
        pass
        #Return value if found, none if not.
        return self._lookup(self.root, key)
    def _lookup(self, node, key):
        ''' Recursively lookup key in Map and return associated value (None if
        missing). '''
        pass
        #base case where node is empty
        if node == None: return None
        #base case when key is found, returns value to top
        if node.key == key: return node.value
        #if key not found and node not empty, BST invariant to left
        if key < node.key:
            return self._lookup(node.left, key)
        
        #if key not found and node not empty, BST invariant to right
        if key > node.key:
            return self._lookup(node.right, key)
    @staticmethod
    def _dump_tree(root):
        ''' Output tree keys in BFS (level-by-level) order.
        - Print out one level per line (with nodes separated by spaces).
        - Do not print any lines with only invalid nodes.
        >>> tree = Node('A', left=Node('B'), right=Node('C'))
        >>> Map._dump_tree(tree)
        A
        B C
        >>> tree = Node('A', left=Node('B', left=Node('C'), right=Node('D')), right=Node('E'))
        >>> Map._dump_tree(tree)
        A
        B E
        C D 0 0
        >>> tree = Node('A', left=Node('B'), right=Node('C', left=Node('D'), right=Node('E')))
        >>> Map._dump_tree(tree)
        A
        B C
        0 0 D E
        '''
        pass
        #Empty dict, queue, and starting tree level of 0
        dict = defaultdict(list)
        queue = deque()
        level = 0
        #start queue with root
        queue.append(root)
        
        
        while queue:
            #level updater. If a level of the tree is fully added to the dict, level index is increased.
            if len(dict[level]) == pow(2, level):
                level += 1
            currNode = queue.popleft()
            #add current key to dict
            dict[level].append(currNode.key)
            #if current key is nothing, do not add its children. (Adds the empty 0 to dict but not children)
            if currNode.key == '0': continue
            
            #Two odd base cases for when a node is set up like a linked list.
            #If a node has no children and the queue is empty, dont add any more trailing empty nodes.
            #If no children and the queue only has another empty node, dont add any more trailing empty nodes.
            #Without these base cases, the loop continues adding empty children to the dictionary forever.
            if not currNode.left and not currNode.right and not queue: continue
            if not currNode.left and not currNode.right and queue == deque([Node('0')]): continue
            #When a node has at least 1 child:
            #check left, append left or empty node
            if currNode.left: queue.append(currNode.left)
            else: queue.append(Node('0'))
            
            #check right, append right or empty node
            if currNode.right: queue.append(currNode.right)
            else: queue.append(Node('0'))
        #When the dictionary is finally sorted by level, this iteration
        #prints each level in order until no more levels are left.
        for value in dict.values():
            if set(value) == {'0'}: continue
            string = " ".join(value)
            print(string)
            
    @staticmethod
    def _rotate_right(p):
        ''' Rotate the sub-tree at parent node to the right.
            P               CL
           / \             /  \
          CL CR     =>    GL   P
         /  \                 / \
        GL  GR              GR   CR
        >>> tree = Node('A', left=Node('B'), right=Node('C'))
        >>> Map._dump_tree(Map._rotate_right(tree))
        B
        0 A
        0 C
        >>> tree = Node('A', left=Node('B', left=Node('C'), right=Node('D')), right=Node('E'))
        >>> Map._dump_tree(Map._rotate_right(tree))
        B
        C A
        0 0 D E
        '''
        pass
        #Takes moved nodes, rotates, and returns the new parent node.
        CL = p.left
        GR = p.left.right
        CL.right = p
        p.left = GR
        return CL
    @staticmethod
    def _rotate_left(p):
        ''' Rotate the sub-tree at parent node to the left.
            P               CR
           / \             /  \
          CL CR     =>    P   GR
            /  \         / \
           GL  GR       CL  GL
        >>> tree = Node('A', left=Node('B'), right=Node('C'))
        >>> Map._dump_tree(Map._rotate_left(tree))
        C
        A 0
        B 0
        >>> tree = Node('A', left=Node('B'), right=Node('C', left=Node('D'), right=Node('E')))
        >>> Map._dump_tree(Map._rotate_left(tree))
        C
        A E
        B D 0 0
        '''
        pass
        #Takes moved nodes, rotates, and returns the new parent node.
        CR = p.right
        GL = p.right.left
        CR.left = p
        p.right = GL
        return CR

