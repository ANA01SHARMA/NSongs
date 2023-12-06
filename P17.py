#Bob has a playlist of N songs, each song has a singer associated with it.
#Favourite singer of Bob is the one whose songs  are the most on the playlist.
#Count the number of Favourite Singers of Bob.

import math
import os
import random
import re
import sys

def sum_of_multiples(n):
    n -= 1
    def sum_divisible_by(p, n=n):
        n = n // p
        return p * (n * (n + 1)) // 2

    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(sum_of_multiples(n))
