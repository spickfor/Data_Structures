#!/usr/bin/env python3


#  Title: closest-numbers.py
#  Abstract: takes list of ints and finds and prints pair of elements that have the smallest difference between them. IF multiple pairs then find all
#  Author: Seth Pickford
#  Email: spickfor@nd.edu
#  Estimate: 2 hrs
#  Date: 3/19/23


def find_min_difference_pair(numbers):
    # Sort the list of numbers
    numbers = sorted(numbers)

    # Initialize the minimum difference to be the difference between the first two elements
    min_diff = abs(numbers[0] - numbers[1])

    # Initialize a list to hold the pairs with the smallest difference
    min_pairs = [(numbers[0], numbers[1])]

    # Iterate over the sorted list of numbers and update the minimum difference and pairs
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])

        if diff < min_diff:
            min_diff = diff
            min_pairs = [(numbers[i], numbers[i+1])]
        elif diff == min_diff:
            min_pairs.append((numbers[i], numbers[i+1]))

    # Return the list of pairs with the smallest difference
    return min_pairs


# Read in the input file
with open('input-closest-numbers.txt', 'r') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().strip().split()))

# Find the pair(s) with the smallest difference
min_pairs = find_min_difference_pair(numbers)

# Print the pairs
for pair in min_pairs:
    print(pair[0], pair[1])

