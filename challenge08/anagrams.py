#!/usr/bin/env python3
'''
Title:      anagrams.py
Abstract:   Determine if two words are anagrams.
Author:     Seth Pickford
Email:      spickfor@nd.edu
Estimate:   1 hour
Date:       04/14/2023
Questions:
    1. What is the worst-case time complexity for count_letters()?
        The worst case time complexity is O(n^2) in which n letters are inserted into a map with worst case insert time complexity of o(n)
    2. What is the worst-case time complexity ofr is_anagram()?
        This function uses two calls of count_letters() (worst case O(n)) and n (n =num unique letters) * two calls of lookup()
        (worst case O(n)), which gives a  worst case time complexity of O(2n +n(2n)), or O(n+n^2)
'''


from treap import Map
import sys
# Functions
def count_letters(word):
    ''' Counts the occurrences of each letter in word and stores it in a Map
    (case insensitive).
    >>> counts = count_letters('aBbCcC')
    >>> counts.lookup('a')
    1
    >>> counts.lookup('b')
    2
    >>> counts.lookup('c')
    3
    >>> counts.lookup('d')
    '''
    pass
    #Initialize empty map, makes the word lowercase (case-sensitive entry)
    m = Map()
    lowerWord = word.lower()
    #inserts each letter into the map with a value of 1.
    #when a letter is already found in the map, increments the value by 1 to count
    #the total instances of that letter.
    for letter in lowerWord:
        m.insert(letter, 1)
    #returns the map
    return m
def is_anagram(word_a, word_b):
    ''' Returns whether or not two words are anagrams.
    >>> is_anagram('anna', 'naan')
    True
    >>> is_anagram('banana', 'aNaNaB')
    True
    >>> is_anagram('SiLeNt', 'listen')
    True
    >>> is_anagram('KeK', 'eek')
    False
    >>> is_anagram('Nope', 'Topen')
    False
    >>> is_anagram('taco', 'cat')
    False
    '''
    pass
    #When two words are not the same length, never an anagram
    if len(word_a) != len(word_b): return False
    #get a map for each word
    count1 = count_letters(word_a)
    count2 = count_letters(word_b)
    #get each letter for comparison from word 1
    lowerWordA = set(word_a.lower())
    #for each possible unique letter, compare values. if at any point the values do not align, return false
    for letter in lowerWordA:
        if count1.lookup(letter) == count2.lookup(letter): continue
        else: return False
    return True
# Main Execution
def main(stream=sys.stdin):
    ''' For each pair of words on each line, determine if they are anagrams,
    and print out the result.
    >>> import io
    >>> main(io.StringIO('taco cat\\nanna naan\\nSiLeNt listen\\n'))
    taco and cat are not anagrams!
    anna and naan are anagrams!
    SiLeNt and listen are anagrams!
    '''
    pass
    for line in stream:
        words = line.split()
        if is_anagram(words[0], words[1]):
            print(f"{words[0]} and {words[1]} are anagrams!")
        else:
            print(f"{words[0]} and {words[1]} are not anagrams!")
        
if __name__ == '__main__':
    main()
