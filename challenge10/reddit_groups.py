#!/usr/bin/env python3

'''
Title:      reddit_groups.py
Abstract:   Determine how many isolated groups are in graph.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   3 hours
Date:       04/30/2023
Questions:

    1. Does it make a difference if you used BFS or DFS for walk_graph?
    Explain.
        An important distinction for this question is that the walk_graph function returns
        a SET, which is unordered by nature. Even though DFS and BFS visit the vertices in a different order,
        the returned set of visited vertices will always be the exact same in functionality because the set is unordered.
        Therefore, whether using DFS or BFS, there is no difference in the returned set of visited vertices.
        

    2. What is the average time complexity of walk_graph?
        The bulk of this function is under a while loop of the frontier variable, which effectively will traverse all
        possible vertices in the graph for n (num vertices) iterations. For each of these iterations, the left of frontier is popped (O(1) with DFS approach),
        this popped vertex is compared with the visited set (O(1) for hash table lookup), it is added to visited if not there already (O(1) add to hash table),
        and finally the vertex's edges are searched (O(1) in hash table lookup) and added to the frontier to be traversed (O(k) for m adjacent edges to current vertex, not constant).
        This results in O(n * (1 + 1 + 1 + k * 1)) = O(n * k) = O(n + m) time complexity on average (where m equals TOTAL number of edges).
        

    3. What is the average time complexity of find_groups?
        For this question, I will use the basis that walk_graph has a time complexity of O(n + m) per my implementation (n = num vertices, m = num edges).
        This function's first loop loops n times (n = total number of vertices) and within this loop, there is:
            1 call to walk_graph O(n + m)
            1 lookup in the groups list O(n) in python list
            1 possible append to groups list O(1)
        The second loop to convert each set in groups to a list (n iterations):
            1 call to edit an indexed item in groups O(1)

        This results in O(n * (n + m + n + 1) + n * 1) = O(2n^2 + nm + 2n) = O(n^2) in this implementation.
'''

import io
import sys

# Functions

def read_graph(stream=sys.stdin):
    ''' Read one graph from the stream.

    >>> read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    {1: [2, 4], 2: [1, 3], 3: [2], 4: [1]}

    >>> read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    {1: [2], 2: [1], 3: [4], 4: [3]}
    '''
    pass
    
    #Try to get num vertices and edges. If value error, stream is improperly formated/non-existant and return None.
    try:
        nVertices = int(stream.readline())
        nEdges = int(stream.readline())
    except ValueError:
        return None

    #dictionary comprehension for graph, has n lists for edge placements
    graph = {n: [] for n in range(1, nVertices + 1)}

    #Loop for number of edges
    for _ in range(nEdges):
        #try to get vertex and edge from stream's current line
        try:
            vert, edge = map(int, stream.readline().strip().split())

        #if failed, stream is improperly formatted/non-existant. return None
        except ValueError:
            return None

        #undirected graph so append to both to track movement both ways along graph
        graph[vert].append(edge)
        graph[edge].append(vert)


    return graph



def walk_graph(graph, origin):
    ''' Perform traversal of graph from origin.

    >>> g = read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    >>> walk_graph(g, 1)
    {1, 2, 3, 4}

    >>> g = read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    >>> walk_graph(g, 1)
    {1, 2}
    '''
    pass
    #Iterative DFS approach to traversal
    #empty set for visited, frontier with origin
    visited = set()
    frontier = [origin]

    while frontier: #while nodes still possible to visit (iterates every node)
        currNode = frontier.pop() #DFS, so pop any possible node

        if currNode in visited: continue #skip node if already seen

        visited.add(currNode) #add to seen

        for edge in graph[currNode]: #append edges to frontier
            frontier.append(edge)

    return visited


def find_groups(graph):
    ''' Find isolated groups in graph.

    >>> g = read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    >>> find_groups(g)
    [[1, 2, 3, 4]]

    >>> g = read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    >>> find_groups(g)
    [[1, 2], [3, 4]]
    '''
    pass
    #empty groups list
    groups = []

    #iterates through total num of vertices
    for i in range(1, len(graph) + 1):

        #potential new group is a set containing all vertices in isolated grouo
        newGroup = walk_graph(graph, i)

        #if the group is already seen (ie, another member of the group has already been walked),
        #continue on to next vertex. else, add this set to total groups.
        if newGroup not in groups:
            groups.append(newGroup)
        else:
            continue
    
    #iterate through all groups to convert sets to lists.
    #Sets are used to make comparisons of the groups easier and not require any sorting since sets are unordered.
    #The doctests require a final list of lists, however, so we convert back to lists here.
    for j in range(len(groups)):
        groups[j] = list(groups[j])

    return groups



# Main Execution

def main(stream=sys.stdin):
    ''' For each graph, find the number of isolated graphs, and print them out
    in sorted order.

    >>> main(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n4\\n2\\n1 2\\n3 4\\n10\\n8\\n1 2\\n6 8\\n8 1\\n10 6\\n7 7\\n7 5\\n3 6\\n6 2\\n'))
    Graph 1:
    1 2 3 4
    Graph 2:
    1 2
    3 4
    Graph 3:
    1 2 3 6 8 10
    4
    5 7
    9
    '''
    pass
    #tracks which graph this is
    numGraph = 1

    #creates graph
    while graph := read_graph(stream):

        #prints graph number
        print(f"Graph {numGraph}:")

        #finds groups in current graph
        groups = find_groups(graph)

        #prints each group formatted with spaces and seperated by a new line
        for group in groups:
            print(" ".join(str(node) for node in group))

        #increment graph number
        numGraph += 1
    

if __name__ == '__main__':
    main()