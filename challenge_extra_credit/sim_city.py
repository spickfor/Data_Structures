#!/usr/bin/env python3

'''
Title:      sim_city.py
Abstract:   Compute the minimum spanning tree of points in a city map.
Author:     Owen Grimaldi
Email:      ogrimald@nd.edu
Estimate:   30 minutes
Date:       12/7/2022
Questions:

    1. What is the average time complexity of build_graph?
        This function returns a dict of dicts with each key value representing a node
        and its dict being the values of distance to every other node and itself. Because this function
        iterates through each point and then all points inside of that loop, it has a time complexity of
        O(V^2).
        ????

    2. What is the average time complexity of compute_mst?
        This function uses Prim's Algorithm exactly, which has a time complexity of
        O(V + ElogE)
        ????

    3. What is the average space complexity of compute_mst?
        This function has a space complexity of O(V + E).
        ????

    4. Does the total cost of the minimum spanning tree change if we use
    different starting vertices isfor compute_mst?  Experiment and then
    explain.
        The total cost of the MST does NOT change if we choose different starting vertices.
        This is because the function will always iterate through the entire graph to find the MST,
        changing starting nodes will only change the shape of the graph. Inherent distances between nodes does not change,
        so while the algorithm may take a different shape to calculate the cost, it will always calculate the lowest possible
        cost (ie, returns the same cost always). 
        ????   
'''

import collections
import heapq
import io
import math
import requests
import sys

# Constants

POINTS_URL  = 'https://yld.me/raw/jpIx'
POINTS_TEXT = requests.get(POINTS_URL).text

# Read Points

def read_points(stream=sys.stdin):
    ''' Read points from stream.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 2.0, 4.0)]

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 1.0, 2.0), (3, 2.0, 1.0)]

    >>> read_points(points_stream)
    [(0, 0.0, 1.0), (1, 2.0, 3.0), (2, 4.0, 1.0), (3, 1.0, 2.0), (4, 5.0, 2.0)]
    '''
    pass

    #try to read source and its location. if not, return none. (wrong format)
    try:
        nPoints = int(stream.readline())
    except ValueError:
        return None

    #initialize
    points = []
    counter = 0
    
    #for each point,
    for _ in range(nPoints):

        #try to map it properly to floats from string
        try:
            xCord, yCord = map(float, stream.readline().split())
        except ValueError:
            return None

        #append counter's cords to points list
        points.append((counter, xCord, yCord))
        
        counter += 1

    return points


# Build Graph

def build_graph(points):
    ''' Build adjacency list from list of points.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 3.1622776601683795}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 2.0}, 2: {0: 3.1622776601683795, 1: 2.0, 2: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 1.0, 3: 1.0}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 1.0, 3: 1.0}, 2: {0: 1.0, 1: 1.0, 2: 0.0, 3: 1.4142135623730951}, 3: {0: 1.0, 1: 1.0, 2: 1.4142135623730951, 3: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 2.8284271247461903, 2: 4.0, 3: 1.4142135623730951, 4: 5.0990195135927845}, 1: {0: 2.8284271247461903, 1: 0.0, 2: 2.8284271247461903, 3: 1.4142135623730951, 4: 3.1622776601683795}, 2: {0: 4.0, 1: 2.8284271247461903, 2: 0.0, 3: 3.1622776601683795, 4: 1.4142135623730951}, 3: {0: 1.4142135623730951, 1: 1.4142135623730951, 2: 3.1622776601683795, 3: 0.0, 4: 4.0}, 4: {0: 5.0990195135927845, 1: 3.1622776601683795, 2: 1.4142135623730951, 3: 4.0, 4: 0.0}})
    '''
    pass

    #counts number of points
    nPoints = points[-1][0] + 1

    #initialize adjacency dict
    graph = collections.defaultdict(dict)

    #iterate through points
    for i in range(nPoints):

        #iterate through points
        for j in range(nPoints):

            #calculate difference in position for x and y, squared
            diffX = pow(points[i][1] - points[j][1], 2)
            diffY = pow(points[i][2] - points[j][2], 2)

            #calculate distance
            distance = math.sqrt(diffX + diffY)

            #set distance in graph.
            graph[i][j] = distance

    return graph

# Compute MST

def compute_mst(graph, start):
    ''' Compute minimum spanning tree.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 1: 0, 2: 1}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 2: 0, 1: 2, 3: 0}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 3: 0, 1: 3, 2: 1, 4: 2}
    '''
    pass

    #vertices to visit and have visited
    frontier = [(0.0, start, start)]
    visited = {}


    while frontier:
        #get data from tuple
        distance, target, source = heapq.heappop(frontier)

        #check if visited. if not, add to visited
        if target in visited: continue
        visited[target] = source

        #adds all neighbors to the frontier for checking
        for neighbor, weight in graph[target].items():
            if neighbor == target: continue
            heapq.heappush(frontier, (weight, neighbor, target))

    return visited


# Main Execution

def main(stream=sys.stdin):
    ''' For each set of points, build the graph, compute the MST, and then
    print out the total cost.

    >>> main(io.StringIO(POINTS_TEXT))
    Graph 1: 3.41
    Graph 2: 3.00
    Graph 3: 7.07
    Graph 4: 12.73
    Graph 5: 27.08
    '''
    pass
    #graph increment
    graphCounter = 1

    #get points for each graph
    while points := read_points(stream):
        #build g raph
        graph = build_graph(points)

        #get MST
        mst = compute_mst(graph, 0)

        cost = 0.0
        #finds distance across the points in order of MST, adds to total cost
        for source, target in mst.items():
            cost += graph[source][target]

        #print and increment for next graph
        print(f"Graph {graphCounter}: {cost:.2f}")

        graphCounter += 1


if __name__ == '__main__':
    main()