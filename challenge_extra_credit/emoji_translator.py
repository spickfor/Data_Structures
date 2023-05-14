#!/usr/bin/env python3

'''
Title:      emoji_translator.py
Abstract:   Translate text commands to emojis.
Author:     Domer McDomerson
Email:      dmcdomer@nd.edu
Estimate:   25 minutes
Date:       11/08/2022
Questions:

    1. What is the average time complexity of substitute_emojis()?
        O(n) as each dict call has complexity of O(1) for n words.
        ????

    2. How did you check if a word was enclosed by ':'?
        I used the startswith() and endswith() methods to check if enclosed by ':'.
        ????

    3. How did you separate the word from the enclosing ':'?
        I used splicing to remove the first and last character of emojis with these colons
        and in the dictionary.
        ????
'''

import sys

# Constants

EMOJIS = {
    'football': '🏈',
    'python'  : '🐍',
    'heart'   : '♥',
    'rocket'  : '🚀',
    'shamrock': '☘',
}

# Functions

def substitute_emojis(text):
    ''' Substitute any words enclosed in : with the corresponding emojis in the
    EMOJIS table.

    If the word is not the table, then return the original word.

    >>> substitute_emojis('i :heart: :python:')
    'i ♥ 🐍'

    >>> substitute_emojis(':shamrock: :Notre: Dame :football: :rocket:\\n')
    '☘ Notre Dame 🏈 🚀'
    '''
    pass
    split = text.split()
    words = []
    for word in split:
        if word.startswith(":") and word.endswith(":") and word[1:-1] in EMOJIS:
            words.append(EMOJIS[word[1:-1]])
        else:
            words.append(word.strip(":"))
    
    newText = " ".join(words)
    return newText


# Main Execution

def main(stream=sys.stdin):
    ''' For each line in standard input, substitute any emojis, and then print
    the translation.

    >>> import io
    >>> main(io.StringIO('i :heart: :python:\\n:shamrock: :Notre: Dame :football: :rocket:\\n'))
    i ♥ 🐍
    ☘ Notre Dame 🏈 🚀
    '''
    pass
    for line in stream:
        print(substitute_emojis(line.strip()))

if __name__ == '__main__':
    main()