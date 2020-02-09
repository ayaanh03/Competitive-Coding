#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'play' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def play(arr):
    tom=0
    jerry=0
    c=0
    done=[]
    max = -1
    maxc= -1
    while(len(done)!=len(arr)):
        print(max,maxc,tom,jerry,done)
        max = -1
        maxc = -1
        for i in range(0,len(arr)):
            if(i not in done):
                for j in range(0,len(arr[0])):
                    if(arr[i][j]>=max):
                        max=arr[i][j]
                        maxc=i
        if(c%2==0):
            tom+=max
        else:
            jerry+=max
        c+=1
        done+=[maxc]
    return abs(tom-jerry)




if __name__ == '__main__':
    fptr = open(os.environ['input001.txt'], 'w')

    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    result = play(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
