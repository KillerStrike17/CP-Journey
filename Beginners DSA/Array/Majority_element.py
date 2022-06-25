from os import *
from sys import *
from collections import *
from math import *


def findMajorityElement(arr, n):
        # Write your code here.
    x = Counter(arr)
    for _ in x.keys():
        if x[_] > n//2:
            return _
    return -1
# 	pass
