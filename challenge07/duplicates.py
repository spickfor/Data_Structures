#!/usr/bin/env python3

'''
Title:      duplicates.py
Abstract:   Determine whether or not a line of words contains any duplicates.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hour
Date:       4/4/2023
Questions:
    1. What is the average time complexity of detect_duplicates()?
        O(nlog(n))
    2. What is the worst-case time complexity of detect_duplicates()?
        O(n^2)
    3. What is the worst-case space complexity of detect_duplicates()?
        O(n)
    4. How would you modify the program to make it case in-sensitive?
        Convert each word to lowercase before processing it.
'''

import sys

# Functions

def detect_duplicates(words):
    '''
    Return whether or not the sequence of words contains a duplicate.
    >>> detect_duplicates('a b c'.split())
    False
    >>> detect_duplicates('a b a'.split())
    True
    >>> detect_duplicates('a b c b e f'.split())
    True
    '''
    word_set = set()
    for word in words:
        word = word.lower()
        if word in word_set:
            return True
        else:
            word_set.add(word)
    return False

# Main Execution

def main(stream=sys.stdin):
    '''
    For each line of words, determine if there are any duplicates.
    >>> import io
    >>> main(io.StringIO('a b c\\na b a\\na b c b e f\\n'))
    False
    True
    True
    '''
    for line in stream:
        words = line.strip().split()
        has_duplicates = detect_duplicates(words)
        print(has_duplicates)

if __name__ == '__main__':
    main()


