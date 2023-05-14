#!/usr/bin/env python3

'''
Title:      cups.py
Abstract:   given the number of cold, water, and hot water cups students want to fill, determine the minimum number of seconds needed to fill up all the cups.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   2 hours
Date:       3/30/23

Questions:
    1. What is the worst-case time complexity of fill_cups()?
        O(nlog(n)) since push and pop are both O(log(n)). 

    2. What is the worst-case space complexity of fill_cups()?
        O(1) because the space required to store elements in the PriorityQueue does not grow with the 
        number of cups

    3. Why is this considered a greedy approach?
        I am trying to fill two types of cups at a time in each iteration making the optimal choice.  
        The optimal choice is always trying to pick the one with the most amount of cups left. I 
        want to minimize the amount of time it takes to fill up all the cups at each step, so I make 
        the best choice possible at each step.
'''

import sys
from priority_queue_heap  import PriorityQueue
# Functions
def fill_cups(cups):
    ''' Return minimum number of seconds required to fill all cups of water.
    Use a greedy algorithm by attempting to fill two types of cups at a time
    until there is only one remaining type.
    >>> fill_cups([1, 4, 2])
    4
    >>> fill_cups([5, 4, 4])
    7
    >>> fill_cups([5, 0, 0])
    5
    '''
    pq = PriorityQueue(cups)
    seconds = 0
    
    while pq.size() > 1:
        cup1 = pq.pop()
        cup2 = pq.pop()
        cup1 -= 1
        cup2 -= 1
        seconds += 1
        
        if cup1 > 0:
            pq.push(cup1)
        if cup2 > 0:
            pq.push(cup2)
    
    if pq.size() == 1:
        seconds += pq.pop()
    return seconds
# Main Execution
def main(stream=sys.stdin):
    ''' For each line of cups, determine the minimum number of seconds required
    to fill all cups of water.
    >>> import io
    >>> main(io.StringIO('1 4 2\\n5 4 4\\n5 0 0\\n'))
    4
    7
    5
    '''
    for line in stream:
        cups = list(map(int, line.split()))
        print(fill_cups(cups))
if __name__ == '__main__':
    main()
