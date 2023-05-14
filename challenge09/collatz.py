#!/usr/bin/env python3

'''
Title:      collatz.py
Abstract:   Compute the Collatz cycle length using memoization.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hoiur
Date:       04/25/2023
Questions:

    1. What is stored in the table passed to cycle_length()?
        The table passed to cycle_length() contains key value pairs with
        the passed integer n as its key and its cycle length count as its value.
        

    2. How is table used in cycle_length() to implement memoization?
        This table caches previously calculated cycle lengths for integers, saving
        the algorithm from repeating a calculation and saving many calls.
        When a cycle length for n is calculated, n and the cycle length are stored as a Pair in the table.
        

    3. What number between 100 and 1000 (inclusive) has the longest cycle
    length?
        871 has the longest cycle length in this range.
        
'''

from table import Map

import sys

# Functions

def cycle_length(n, table):
    ''' Return the collatz cycle length.

    >>> cycle_length(22, Map())
    16

    >>> cycle_length(58, Map())
    20

    >>> cycle_length(71, Map())
    103

    >>> cycle_length(1337, Map())
    45
    '''
    pass
    #base case (testing desires that cycle length at 1 is 1)
    if n == 1: return 1

    #if the value is not in the table,
    if table.lookup(str(n)) == None:
        #if odd, insert n with the cycle length of n/2
        if n % 2 == 0: table.insert(str(n), cycle_length(n/2, table))
        #if even, insert n with cycle length of 3n + 1
        else: table.insert(str(n), cycle_length(3*n + 1, table))

    #return cycle length of n + 1
    return table.lookup(str(n)) + 1


# Main Execution

def main(stream=sys.stdin):
    ''' For each number in standard input, compute the cycle length, and print
    it out.

    >>> import io
    >>> main(io.StringIO('22\\n58\\n71\\n1337\\n'))
    Cycle Length of 22: 16
    Cycle Length of 58: 20
    Cycle Length of 71: 103
    Cycle Length of 1337: 45
    '''
    pass
    for line in stream:
        print(f"Cycle Length of {line.strip()}: {cycle_length(int(line.strip()), Map())}")

if __name__ == '__main__':
    main()