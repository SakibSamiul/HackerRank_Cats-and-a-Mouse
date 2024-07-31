#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if x > z:
        cat_a = x-z
    else:
        cat_a = z-x
    if y > z:
        cat_b = y - z
    else:
        cat_b = z - y

    if cat_a > cat_b:
        print("Cat B")
    elif cat_b > cat_a:
        print("Cat A")
    else:
        print("Mouse C")
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

    #     fptr.write(result + '\n')

    # fptr.close()
