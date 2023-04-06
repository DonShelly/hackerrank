#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    # Write your code here
    for number in arr:
        if number > 0:
            positive = positive + 1
        elif number < 0:
            negative = negative + 1
        else:
            zero = zero + 1
    print("{:.6f}".format(positive/len(arr)))
    print("{:.6f}".format(negative/len(arr)))
    print("{:.6f}".format(zero/len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
