'''
Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
Declare an integer, , and initialize it to .

There are  types of queries, given as an array of strings for you to parse:

Query: 1 x y
Let .
Append the integer  to .
Query: 2 x y
Let .
Assign the value  to .
Store the new value of  to an answers array.
Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.
Finally, size(arr[idx]) is the number of elements in arr[idx]

Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in 
- string queries[q]: query strings that contain 3 space-separated integers

Returns

int[]: the results of each type 2 query in the order they are presented
Input Format

The first line contains two space-separated integers, , the size of  to create, and , the number of queries, respectively.
Each of the  subsequent lines contains a query string, .

Constraints

It is guaranteed that query type  will never query an empty array or index.
Sample Input

2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
Sample Output

7
3
Explanation

Initial Values:


 = [ ]
 = [ ]

Query 0: Append  to .

 = [5]
 = [ ]

Query 1: Append  to .
 = [5]
 = [7]

Query 2: Append  to .

 = [5, 3]
 = [7]

Query 3: Assign the value at index  of  to , print .

 = [5, 3]
 = [7]

7
Query 4: Assign the value at index  of  to , print .

 = [5, 3]
 = [7]

3
'''


#!/bin/python3

import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    lastanswer=0
    arr=[[] for _ in range(n)]
    
    for q in queries:
        op,x,y=q
        if op==1:
            arr[(x^lastanswer)%n].append(y)
        elif op==2:
            s=arr[(x^lastanswer)%n]
            lastanswer=s[y%len(s)]
            print(lastanswer)

if __name__ == '__main__':

    n,q = map(int,input().rstrip().split())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    dynamicArray(n, queries)
