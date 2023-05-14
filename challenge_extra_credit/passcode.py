#!/usr/bin/env python3

'''
Title:      passcode.py
Abstract:   Use topological sort to crack the passcode.
Author:     Owen Grimaldi
Email:      ogrimald@nd.edu
Estimate:   30 minutes
Date:       12/7/2022
Questions:

    1. What does compute_degrees produce?
        This function produces a defaultdict with each key being a vertex and its value
        being the number of degrees (edges) that this vertex is in contact with.
        ????

    2. What is the average time complexity of compute_degrees?
        If v is to represent the number of vertices and e represents the number of
        degrees each vertex has, then the time complexity of this function is O(V + E)
        as it iterates through v keys and within each loop, iterates through e degrees that v has.
        ????

    3. What is the average time complexity of topological sort?
        This function uses Khan's algorithm, which has a time complexity of
        O(|V| + |E|). (One loop for calculating degrees, other for sort. Each has O(V + E), so O(2 * (V + E) or total of O(V + E))
        ????

    4. What is the average space complexity of topological sort?
        The function needs to store all of the vertices, which gives it a space complexity of
        O(|V|).
        ????
'''

import collections
import io
import sys

# Constants

SAMPLE_CODES = [352, 154, 542, 315, 152]
LONGER_CODES = [219, 183, 804, 376, '043', 904, 357, 857, 206, 180, 983, 284, 843]

# Functions

def read_graph(stream=sys.stdin):
    ''' Read codes into graph (adjacency set).

    >>> read_graph(io.StringIO('\\n'.join(map(str, SAMPLE_CODES))))
    defaultdict(<class 'set'>, {3: {1, 5}, 5: {2, 4}, 1: {5}, 4: {2}})

    >>> read_graph(io.StringIO('\\n'.join(map(str, LONGER_CODES))))
    defaultdict(<class 'set'>, {2: {0, 1, 8}, 1: {8, 9}, 8: {0, 3, 4, 5}, 0: {4, 6}, 3: {5, 7}, 7: {6}, 4: {3}, 9: {0, 8}, 5: {7}})
    '''
    pass

    #graph initialized
    graph = collections.defaultdict(set)

    #loops until if statement break, which occurs when no more codes are input.
    while True:

        #read code and strip to string of numbers
        currCode = stream.readline().strip()

        #check if input is a code. end function and return graph if all codes read
        if (currCode == "") or (not currCode):
            return graph
        
        #creates a list of str numbers
        currCode = list(currCode)

        #individual variables for numbers, all ints
        firstNum, secondNum, thirdNum = list(map(int, currCode))
        
        #proper graph allocation
        graph[firstNum].add(secondNum)
        graph[secondNum].add(thirdNum)


def compute_degrees(graph):
    ''' Compute degrees of all vertices in graph.

    >>> compute_degrees(read_graph(io.StringIO('\\n'.join(map(str, SAMPLE_CODES)))))
    defaultdict(<class 'int'>, {3: 0, 1: 1, 5: 2, 2: 2, 4: 1})

    >>> compute_degrees(read_graph(io.StringIO('\\n'.join(map(str, LONGER_CODES)))))
    defaultdict(<class 'int'>, {2: 0, 0: 3, 1: 1, 8: 3, 9: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2})
    '''
    pass

    #initialized dd for ints
    degrees = collections.defaultdict(int)

    #loops for each key - dict pair in graph
    for key, vertices in graph.items():

        #checks if already in degrees. if not, set to 0. (accounts for 3 and 2 in doctests)
        if key not in degrees:
            degrees[key] = 0

        #For each connection in the graph sets, increment degrees counter
        for item in vertices:
            degrees[item] += 1

    return degrees


def topological_sort(graph):
    ''' Perform a topological sort on graph.

    >>> topological_sort(read_graph(io.StringIO('\\n'.join(map(str, SAMPLE_CODES)))))
    [3, 1, 5, 4, 2]

    >>> topological_sort(read_graph(io.StringIO('\\n'.join(map(str, LONGER_CODES)))))
    [2, 1, 9, 8, 0, 4, 3, 5, 7, 6]
    '''
    pass

    #get degrees of graph
    degrees = compute_degrees(graph)

    #frontier and visited lists
    frontier = [v for v, d in degrees.items() if d == 0]
    visited = []

    #while remaining degrees
    while frontier:
        #get current node, note it as seen
        vertex = frontier.pop()
        visited.append(vertex)

        #iterates neighbors of current vertex
        for neighbor in graph[vertex]:

            #increment degrees. if 0, append to frontier for visited addition
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                frontier.append(neighbor)
    
    return visited


# Main Execution

def main(stream=sys.stdin):
    ''' Read graph from passcodes, perform topological sort, and print original
    full passcode.

    >>> main(io.StringIO('\\n'.join(map(str, SAMPLE_CODES))))
    31542

    >>> main(io.StringIO('\\n'.join(map(str, LONGER_CODES))))
    2198043576
    '''
    pass

    #get graph
    graph = read_graph(stream)

    #get full code sorted
    codeList = topological_sort(graph)

    #join code numbers into a string, print
    print("".join(map(str, codeList)))

if __name__ == '__main__':
    main()