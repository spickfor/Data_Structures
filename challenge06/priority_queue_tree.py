'''
Title:      priority_queue_tree.py
Abstract:   Implement a priority queue using an array-based binary tree.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hours
Date:       03/30/23
Questions:
    1. While performing a BFS, how do you know if node is valid or not?
        Usually, some sort of data structure is kept to track visited nodes and make sure that they aren't revisited.
        This prevents unnecessary traversals or infinite loops.

    2. What is the worst-case time complexity of PriorityQueue.pop()? 
        O(log(n)) is the worst case.  n is the number of elements in queue.

    3. What is the worst-case space complexity of PriorityQueue.pop()?
        0(1) is the worst case. n is the number of elements in queue.
'''

from collections import deque
# Classes
class PriorityQueue:
    ''' Simple priority queue using an array-based binary tree. '''
    def __init__(self, tree):
        ''' Initialize internal binary tree.
        >>> pq = PriorityQueue([4, 6, 6, 3, 7]); pq.tree
        [4, 6, 6, 3, 7]
        '''
        self.tree = tree
    def pop(self):
        ''' Return the largest value in priority queue.
        Walk tree using BFS to find largest value, place 0 in its place, and
        then return largest value.
        >>> pq = PriorityQueue([4, 6, 6, 3, 7])
        >>> [pq.pop(), pq.pop(), pq.pop(), pq.pop(), pq.pop()]
        [7, 6, 6, 4, 3]
        >>> pq.tree
        [0, 0, 0, 0, 0]
        '''
        if not self.tree:
           return None
        queue = deque([0])
        max_value = self.tree[0]
        max_index = 0
        while queue:
            index = queue.popleft()
            value = self.tree[index]
            if value > max_value:
                max_value = value
                max_index = index
            left = left_child(index)
            right = right_child(index)
            if left < len(self.tree):
                queue.append(left)
            if right < len(self.tree):
                queue.append(right)
        self.tree[max_index] = 0
        return max_value
# Functions
def left_child(index):
    ''' Return index of left child.
    >>> left_child(0)
    1
    >>> left_child(1)
    3
    '''
    return 2 * index + 1
def right_child(index):
    ''' Return index of right child.
    >>> right_child(0)
    2
    >>> right_child(1)
    4
    '''
    return 2 * index + 2
