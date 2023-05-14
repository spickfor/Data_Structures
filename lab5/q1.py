#!/usr/bin/env python3


def countEvens(array):
    if len(array) == 0:
        return 0
    if array[0] % 2 == 0:
        return 1 + countEvens(array[1:])
    else:
        return countEvens(array[1:])


def sumEvens(array):
    if len(array) == 0:
        return 0
    if array[0] % 2 == 0:
        return array[0] + sumEvens(array[1:])
    else:
        return sumEvens(array[1:])


def printEvens(array):
    if len(array) == 0:
        return
    if array[-1] % 2 == 0:
        print(array[-1])
    printEvens(array[:-1])


def printEvensInOrder(array, current):
    if current == len(array):
        return
    if array[current] % 2 == 0:
        print(array[current])
    printEvensInOrder(array, current+1)


def isPrime(base, divisor=2):
    if base < 2:
        return False
    if divisor * divisor > base:
        return True
    if base % divisor == 0:
        return False
    return isPrime(base, divisor+1)


def factorNumber(number, factor=2, count=0):
    if number < 2:
        return count
    if number % factor == 0:
        print(factor)
        count += 1
        return factorNumber(number/factor, factor, count)
    else:
        return factorNumber(number, factor+1, count)


def main():
    print("Count evens")
    count1 = countEvens([1, 2, 3, 4, 5, 6])
    print(count1)

    print("sum evens")
    count2 = sumEvens([1, 2, 3, 4, 5, 6])
    print(count2)

    print("print evens")
    printEvens([1, 2, 3, 4, 5, 6])

    print("print evens ordered")
    printEvensInOrder([1, 2, 3, 4, 5, 6], 0)

    print("isprime")
    primeval = isPrime(7)
    print(primeval)

    print("factor Number")
    factor = factorNumber(6)
    print(factor)



main()