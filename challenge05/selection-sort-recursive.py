#!/usr/bin/env python3


#  Title: selection-sort-recursion.py
#  Abstract: implement selection sort on inputs from user
#  Author: Seth Pickford
#  Email: spickfor@nd.edu
#  Estimate: 1 hrs
#  Date: 3/19/23


def selection_sort_recursive(arr, n, index=0):
    if index == n:
        return

    min_index = index
    for i in range(index + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    arr[min_index], arr[index] = arr[index], arr[min_index]

    selection_sort_recursive(arr, n, index + 1)

def main():
    numbers = input("Enter a list of integers separated by space: ")
    int_list = [int(x) for x in numbers.split()]

    sorted_list1 = int_list.copy()

    selection_sort_recursive(sorted_list1, len(sorted_list1))

    print(f"Recursive Selection Sort: {sorted_list1}")

if __name__ == "__main__":
    main()
