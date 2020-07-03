#!/usr/bin/env python3


class bun:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is: {self._n}'

    def __str__(self):
        return f'set: the number of bunnies is: {self._n}'


x = bun(47)
print(chr(128406))
