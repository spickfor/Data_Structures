#!/usr/bin/env python3

'''
Title:      balanced.py
Abstract:   Determine wether or not a binary tree is balanced.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hour
Date:       4/4/2023
Questions:
    1. What is the worst-case time complexity of is_balanced()?
        O(n)
    2. What information does is_balanced() return?
        A tuple containing a boolean indicating whether the tree is balanced and an integer representing the height of the tree
'''

import sys

# Functions

def is_balanced(array, index=0):
    '''
    Determine whether or not a binary tree is balanced.
    A binary tree is balanced if:
    1. Left and right sub-trees are balanced.
    2. Difference between heights of left and right sub-trees is no more than 1.
    >>> is_balanced([5, 3, 6])
    (True, 2)
    >>> is_balanced([5, 3, 6, 4])
    (True, 3)
    >>> is_balanced([5, 3, 0, 4])
    (False, 3)
    >>> is_balanced([5, 3, 4, 0, 1])
    (True, 3)
    >>> is_balanced([5, 3, 4, 0, 1, 0, 0, 0, 0, 2])
    (False, 4)
    '''
    if index >= len(array) or array[index] == 0:
        return True, 0

    left_balanced, left_height = is_balanced(array, 2 * index + 1)
    right_balanced, right_height = is_balanced(array, 2 * index + 2)

    balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    height = max(left_height, right_height) + 1

    return balanced, height

# Main Execution

def main(stream=sys.stdin):
    '''
    For each line with a tree given in BFS format, output whether or not it
    is balanced.
    >>> import io
    >>> main(io.StringIO('5 3 6\\n5 3 6 4\\n5 3 0 4\\n'))
    Balanced
    Balanced
    Not Balanced
    '''
    for line in stream:
        tree = list(map(int, line.split()))
        balanced, _ = is_balanced(tree)
        print("Balanced" if balanced else "Not Balanced")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
