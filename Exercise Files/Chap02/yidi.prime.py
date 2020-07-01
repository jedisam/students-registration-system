#!/usr/bin/env python3

def primeChecker(x):
    check = 1
    count = 0
    while check < x:
        if x % check == 0:
            count = count + 1
        check = check + 1
    if count == 1:
        return True
    elif count > 1:
        return False


def list_prime(num):
    first = 2
    while first < num:
        if primeChecker(first):
            print(first, end=' ', flush=True)
        first = first + 1
    print()


list_prime(144)
