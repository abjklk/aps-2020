#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    f=(n*(n+1))//2
    f=f**2
    s=(n*(n+1)*(2*n+1))//6
    print(f-s)