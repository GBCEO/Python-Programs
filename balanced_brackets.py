#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    open_brackets = ['{','(','[']
    dict_brackets = {'}':'{',')':'(',']':'['}
    open_stack = []
    for c in s:
        if c in open_brackets:
            open_stack.append(c)
        else:
            if len(open_stack)==0 or dict_brackets[c] != open_stack.pop():
                return "NO"
    if len(open_stack)!=0:
        return "NO"
    return "YES"

    return "YES"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
