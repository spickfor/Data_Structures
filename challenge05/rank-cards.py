#!/usr/bin/env python3


#  Title: rank-cards.py
#  Abstract: ranks cards and prints out names of cardholders in the order of card rankings
#  Author: Seth Pickford
#  Email: spickfor@nd.edu
#  Estimate: 2 hrs
#  Date: 3/19/23


def rank_card(card):
    rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suit_order = {'C': 1, 'D': 2, 'H': 3, 'S': 4}

    rank = ''.join([c for c in card if c.isdigit() or c == 'A' or c == 'K' or c == 'Q' or c == 'J'])
    suit = card[-1]
    
    return rank_order[rank], suit_order[suit]

def read_and_rank_cards(filename):
    with open(filename, 'r') as file:
        num_hands = int(file.readline().strip())
        hands = []

        for line in file:
            data = line.strip().split()
            if len(data) == 3:
                name, rank, suit = data
                hands.append((name, rank + suit))

        hands.sort(key=lambda hand: rank_card(hand[1]), reverse=True)

        return ', '.join([hand[0] for hand in hands])

def main():
    input_file = 'input-rank-cards.txt'
    sorted_cardholders = read_and_rank_cards(input_file)
    print(sorted_cardholders)

if __name__ == '__main__':
    main()
