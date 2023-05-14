#!/usr/bin/env python3

'''
Title:      table.py
Abstract:   Implement a Map class using a hash table with separate chaining.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hours
Date:       04/25/2023
Questions:

    1. What is worst-case time complexity of Map.insert()?
        The worst case time complexity for insert is O(n), in which
        every value in the map is in the same bucket and all n keys in the bucket must
        be compared for insertion.
        

    2. What is worst-case time complexity of Map.lookup()?
        This function also has a worst-case of O(n) in which you have to search through all n
        items in the desired bucket to compare key values of the pair and lookup key.
        

    3. What is the load factor of a hash table?
        The load factor of a hash table is a measure of its occupancy, being the number of pairs
        divided by number of buckets in this specific implementation.
        

    4. To ensure the time complexities stated above, what must the hash table
    do internally when the load factor reaches a certain threshold?
        When the load factor reaches a certain threshold, the hash table must resize itself
        by doubling the number of buckets and re-inserting every element already in the hash table.
        
'''

from dataclasses import dataclass

# Constants

FNV_OFFSET_BASIS = 14695981039346656037
FNV_PRIME        = 1099511628211

# Classes

@dataclass
class Pair:
    ''' Pair with string key and integer value. '''
    pass
    #new pair
    key: str = None
    value: int = None

class Map:
    ''' Map Implementation based on a hash table. '''

    LOAD_FACTOR = 1.5

    def __init__(self, nbuckets=8):
        ''' Initialize empty Map.

        >>> m = Map()
        >>> len(m.buckets)
        8

        >>> m = Map(4)
        >>> m.buckets
        [[], [], [], []]
        >>> m.size
        0
        '''
        #creates number of buckets and sets size to 0
        self.buckets = [[] for _ in range(nbuckets)]
        self.size = 0


    def insert(self, key, value):
        ''' Insert key, value pair into Map.  If key is already in Map, then
        update value.

        >>> m = Map()
        >>> m.insert('D', 0); m.buckets[3]
        [Pair(key='D', value=0)]
        >>> m.size
        1

        >>> m.insert('F', 1); m.buckets[1]
        [Pair(key='F', value=1)]
        >>> m.size
        2

        >>> m.insert('H', 2); m.buckets[7]
        [Pair(key='H', value=2)]
        >>> m.size
        3

        >>> m.insert('C', 3); m.buckets[2]
        [Pair(key='C', value=3)]
        >>> m.size
        4

        >>> m.insert('A', 4); m.buckets[4]
        [Pair(key='A', value=4)]
        >>> m.size
        5

        >>> m.insert('A', 6); m.buckets[4]
        [Pair(key='A', value=6)]
        >>> m.size
        5
        '''
        #checks if load factor has been reached. resize if so
        if self.size // len(self.buckets) > self.LOAD_FACTOR: self.resize()

        #buckets index calc
        bucket = self.hash(key) % len(self.buckets)
        
        #for each pair in the bucket, check if key == key. if so, update value and not size
        for pair in self.buckets[bucket]:
            if pair.key == key:
                pair.value = value
                return

        #else, add pair to bucket with key and value and update size
        self.buckets[bucket].append(Pair(key, value))
        self.size += 1


    def lookup(self, key):
        ''' Lookup key in Map and return associated value (None if missing).

        >>> m = Map()
        >>> d = [('sbn', 574), ('eau', 715), ('sna', 714), ('nyc', 646)]
        >>> for k, v in d: m.insert(k, v)
        >>> all(m.lookup(k) == v for k, v in d)
        True

        >>> m.lookup('stl')
        '''
        #calculate bucket
        bucket = self.hash(key) % len(self.buckets)

        #for each pair in bucket, check if key == key. If so, return value. Else, return None
        for pair in self.buckets[bucket]:
            if pair.key == key: return pair.value
        return None


    def resize(self):
        ''' Resize the hash table by creating a new buckets array that is twice
        as large, rehashing the existing Pairs into the new buckets array, and
        then reassigning the internal buckets array to this new array.

        >>> m = Map(2)
        >>> d = [('sbn', 574), ('eau', 715), ('sna', 714), ('nyc', 646), ('stl', 314)]
        >>> for k, v in d: m.insert(k, v)
        >>> len(m.buckets)
        4
        >>> all(m.lookup(k) == v for k, v in d)
        True
        '''
        #make copy of current hash table
        oldBuckets = self.buckets

        #set hash table to new hash table with 2 times number of buckets
        self.buckets = [[] for i in range(2 * len(self.buckets))]

        #Insert all pairs into new hash table
        for bucket in oldBuckets:
            for item in bucket:
                self.insert(item.key, item.value)


        

    @staticmethod
    def hash(d):
        ''' Compute the FNV-1a hash on the string or int d.

        >>> Map.hash('notre')
        4751529075592153558511737267927

        >>> Map.hash('dame')
        16047809754340873646920371502188

        >>> Map.hash(574)
        10222938680436398074917206614173
        '''
        #follows PC guide for custom hash method
        if isinstance(d, str):
            d = d.encode()
        hash = FNV_OFFSET_BASIS
        for byte in bytes(d):
            hash = hash ^ byte
            hash = (hash % (pow(2, 64))) * FNV_PRIME
        return hash
        pass