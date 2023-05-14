#!/usr/bin/env python3


#  Title: insertion-sort-recursion.py
#  Abstract: implement insertion sort on inputs from user
#  Author: Seth Pickford
#  Email: spickfor@nd.edu
#  Estimate: 1 hrs
#  Date: 3/19/23


def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    
    insertion_sort_recursive(arr, n - 1)

    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


def main():
    numbers = input("Enter a list of integers separated by space: ")
    int_list = [int(x) for x in numbers.split()]

    sorted_list1 = int_list.copy()

    insertion_sort_recursive(sorted_list1, len(sorted_list1))

    print(f"Recursive Insertion Sort: {sorted_list1}")

if __name__ == "__main__":
    main()
