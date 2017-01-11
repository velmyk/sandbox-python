#!/usr/bin/env python3
'''Returns all prime numbers from the given range.

Usage:
    python3 comprehensions.py number
'''


import sys
from math import sqrt

def is_prime(number):
    '''Finds out if number is prime.

    Args:
        number: End of range to find prime numbers in.

    Returns:
        A list of prime numbers of given range.
    '''
    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(number):
    '''Finds prime numbers in range.'''
    print([x for x in range(int(number)) if is_prime(x)])

if __name__ == '__main__':
    find_primes(sys.argv[1])
