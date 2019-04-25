#!/bin/python3
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    result = 0
    lastnum = 0
    for n in sorted(ar):
        print ('number {}'.format(n))
        if n == lastnum:
            result = result + 1
            print('Lastnum is {} n is {}'.format(lastnum, n))
            lastnum = 0
        else:
            lastnum = n
            print('Lastnum is {} n is {}'.format(lastnum, n))
            lastnum = n
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
