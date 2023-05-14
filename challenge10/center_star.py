#!/usr/bin/env python3

'''
Title:      center_star.py
Abstract:   Determine center of star graph.
Author:     Seth Pickford
Email:      spickford@nd.edu
Estimate:   3 hours
Date:       04/30/2023
Questions:

    1. If you did not use a defaultdict to represent the graph, how else could
    you have added the edges to the adjaceny list (describe one alternative
    approach)?
        Without access to defaultdict, one could use the exact same process to add edges
        to the adjaceny list using a normal dictionary. Whenever adding an edge to a vertex in the
        adjacency list, you can check whether a vertex is in the dictionary with "if vertex in dict:".
        If vertex is in the dict already, you can append the edges accordingly (would have to check if edge in dict as well if undirected graph).
        If not in the dict, you can set dict[vertex] to an empty list and append the edge to the list (vice versa for undirected graph).

        A simplier way to implement this functionality without a defaultdict would be to use dictionary
        comprehension assuming you know the number of vertices. By creating graph to be a dictionary with
        n keys from 1 to n, you can set each of their values to an empty list and then append the edges and vertices
        accordingly. Syntax example: graph = {n: [] for n in range(1, nVertices + 1)}


    2. What is the average time complexity of find_center?
        find_center() has an average time complexity of O(n) where n is the number of vertices.
        In this function, each of the graph's keys (or each vertex) is checked to see if they have
        n - 1 edges per the length of their neighbors list. The call to this neighbor's list is O(1) as
        the defaultdict uses a hash table, so for each of n calls to the key, there is constant operations occurring.
        Therefore, the function is O(1 * n) or O(n).

'''

import io
import sys

from collections import defaultdict

# Functions

def read_graph(stream=sys.stdin):
    ''' Read one graph from the stream.

    >>> read_graph(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n'))
    defaultdict(<class 'list'>, {1: [2], 2: [1, 3, 4], 3: [2], 4: [2]})

    >>> read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n1 4\\n'))
    defaultdict(<class 'list'>, {1: [2, 5, 3, 4], 2: [1], 5: [1], 3: [1], 4: [1]})

    >>> read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n2 4\\n'))
    defaultdict(<class 'list'>, {1: [2, 5, 3], 2: [1, 4], 5: [1], 3: [1], 4: [2]})
    '''
    pass

    #adjacency list implementation for graph
    graph = defaultdict(list)

    #try to get edges. if formatted wrong or non-existant graph, return None
    try:
        nEdges = int(stream.readline())
    except ValueError:
        return None

    #iterate through num edges
    for _ in range(nEdges):

        #for each edge, get the vertex and edge in two int variables.
        #if fails, formatted wrong or non-existant graph, return None
        try:
            source, target = map(int, stream.readline().split())

        except ValueError:
            return None

        #undirected graph, so both values are connected to one another and marked as such in graph
        graph[source].append(target)
        graph[target].append(source)


    return graph
    



def find_center(graph):
    ''' Find center vertex of star graph.

    >>> find_center(read_graph(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n')))
    2

    >>> find_center(read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n1 4\\n')))
    1

    >>> find_center(read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n2 4\\n')))
    '''
    pass

    #for each vertex (key = vertex in graph dict)
    for key in graph.keys():
        #len(graph[key]) returns the number of edges each vertex has.
        #because the center is defined as having N (num vertices) - 1 edges, if the aforementioned length
        #is equal to N - 1, return this vertex as the center. If no center, return none.
        if len(graph[key]) == (len(graph) - 1):
            return key
    
    return None





# Main Execution

def main(stream=sys.stdin):
    ''' For each graph, determine which vertex is the center of the star graph,
    and print it out.

    >>> main(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n4\\n1 2\\n5 1\\n1 3\\n1 4\\n4\\n1 2\\n5 1\\n1 3\\n2 4\\n'))
    Vertex 2 is the center
    Vertex 1 is the center
    There is no center
    '''
    pass

    #for each graph in stream,
    while graph := read_graph(stream):

        #find center of current graph
        center = find_center(graph)
        
        #if center exists, print formatted string
        if center:
            print(f"Vertex {center} is the center")
        #else, indicate no center
        else:
            print("There is no center")

if __name__ == '__main__':
    main()

