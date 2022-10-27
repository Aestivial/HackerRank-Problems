#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    k = int(input())
    se = []
    for i in arr:
        se.append(i[k])
    se.sort()
    final=[]
    for i in se:
        for j in arr:
            if i==j[k]:
                final.append(j)
                arr.remove(j)
                break
            else:
                continue
    for i in final:     
        print(*i)
