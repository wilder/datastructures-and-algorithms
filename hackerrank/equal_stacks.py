#!/bin/python
def equal_height(stk1, stk2, stk3):
    if (not stk1) or (not stk2) or (not stk3):
        return 0
    
    sum1, sum2, sum3 = sum(stk1), sum(stk2), sum(stk3)

    #while they're different
    while (sum1 != sum2) or (sum2 != sum3) or (sum1 != sum3):
        if sum1 >= sum2 and sum1 >= sum3:
            sum1-= stk1.pop()

        elif sum2 >= sum1 and sum1 >= sum3:
            sum2-= stk2.pop()
        
        else:
            sum3-= stk3.pop()
    
    return sum1

import sys

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
print equal_height(h1[::-1], h2[::-1], h3[::-1])
