#!/usr/bin/env python3
'''
Title:      invert.py
Abstract:   Invert binary tree.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hour
Date:       11/01/2022
Questions:
    1. What is the worst-case time complexity of tree_invert()?
        0(n)
    2. How do you swap two values in Python without a temporary value?
        You can swap two values without a temporary variable by using tuple unpacking
'''
import sys
from collections import deque
# Functions
def tree_invert(node):
    ''' Invert tree in-place using divide and conquere.
    >>> tree_walk(tree_invert(tree_read([1, 2, 3])))
    '1, 3, 2'
    >>> tree_walk(tree_invert(tree_read([1, 2, 3, 4, 0, 0, 6])))
    '1, 3, 2, 6, 0, 0, 4'
    '''
    if not node:
        return None
    node[1], node[2] = node[2], node[1]
    tree_invert(node[1])
    tree_invert(node[2])
    return node
def tree_read(data):
    nodes = [([v, None, None] if v != 0 else None) for v in data]
    for i, node in enumerate(nodes[:len(data)//2]):
        if node:
            node[1] = nodes[i * 2 + 1]
            node[2] = nodes[i * 2 + 2]
    return nodes[0]
def tree_walk(node):
    if not node:
        return ''
    result = []
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current:
            result.append(str(current[0]))
            queue.append(current[1])
            queue.append(current[2])
        else:
            result.append('0')
    while result[-1] == '0':
        result.pop()
    return ', '.join(result)
# Main Execution
def main(stream=sys.stdin):
    ''' For each line, read in the tree in BFS format, print it, invert it, and
    then print it again.
    >>> import io
    >>> main(io.StringIO('1 2 3\\n1 2 3 4 0 0 6\\n'))
    1, 2, 3
    1, 3, 2
    1, 2, 3, 4, 0, 0, 6
    1, 3, 2, 6, 0, 0, 4
    '''
    for line in stream:
        tree_data = list(map(int, line.strip().split()))
        tree = tree_read(tree_data)
        print(tree_walk(tree))
        inverted_tree = tree_invert(tree)
        print(tree_walk(inverted_tree))
if __name__ == '__main__':
    main()

