#!/usr/bin/env python3

'''
Title:      happy_numbers.py
Abstract:   Determine if a number is a happy number or not using memoization.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hour
Date:       04/25/2023
Questions:

    1. How is seen used in is_happy()?
        Seen is used to check whether or not the integer being passed to is_happy()
        has already been checked for happiness. If so and the number is not happy, this would indicate a loop and
        the loop is stopped by returning False.


    2. How is table used in is_happy() to implement memoization?
        The table retains information as to whether or not the given integer being passed to is_happy()
        is already found to be happy. If so, then we do not need to recurse until 1 and we simply return True.
        This implementation of memoization saves additional calls by checking if the "truth value of happiness"
        has already been calculated and returns if so.


    3. How many happy numbers are there between 1 and 100 (inclusive)?
        There are 20 happy numbers between 1 and 100 (inclusive).
        
'''

from table import Map

import sys

# Functions

def is_happy(n, seen, table):
    ''' Return whether or not n is a happy number.

    >>> is_happy(19, Map(), Map())
    True

    >>> is_happy(2, Map(), Map())
    False

    >>> is_happy(68, Map(), Map())
    True

    >>> is_happy(75, Map(), Map())
    False

    >>> is_happy(91, Map(), Map())
    True
    '''
    pass

    #Base cases, checks if n already checked for happiness and
    #if n already seen and not checked for happiness, prevents loop by returning false
    if table.lookup(str(n)) != None: 
        return True
    if seen.lookup(str(n)): 
        return False

    #Calculates new total (all digits squared and summed)
    digits = list(map(int, str(n)))
    for i in range(len(digits)):
        digits[i] = digits[i] * digits[i]
    total = sum(digits)

    #shows n as seen
    seen.insert(str(n), 1)

    #if total is 1, clock value as happy and return true
    if total == 1:
        table.insert(str(n), 1)
        return True

    #if reaches this point, check if total is happy
    if is_happy(total, table, seen):
        #if so, memoize that n is also happy and return True
        table.insert(str(n), 1)
        return True
    else:
        return False
# Main Execution

def main(stream=sys.stdin):
    ''' For each number in standard input, determine if it is a happy number,
    and print it out.

    >>> import io
    >>> main(io.StringIO('19\\n2\\n68\\n75\\n91\\n'))
    Is 19 Happy?: Yes
    Is 2 Happy?: No
    Is 68 Happy?: Yes
    Is 75 Happy?: No
    Is 91 Happy?: Yes
    '''
    pass
    #for each line, check if int is happy. print accordingly
    for line in stream:
        if is_happy(int(line.strip()), Map(), Map()):
            print(f"Is {line.strip()} Happy?: Yes")
        else:
            print(f"Is {line.strip()} Happy?: No")

if __name__ == '__main__':
    main()