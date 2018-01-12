'''
You are given container full of water. Container can have limited amount of water. You also have 
N
N bottles to fill. You need to find the maximum numbers of bottles you can fill.

Input:
First line contains one integer, 
T
T, number of test cases.
First line of each test case contains two integer, 
N
N and 
X
X, number of bottles and capacity of the container.
Second line of each test case contains 
N
N space separated integers, capacities of bottles.

Output:
For each test case print the maximum number of bottles you can fill.

https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/tutorial/
'''

test_cases = int(raw_input())
for t in range(test_cases):
    filled = 0
    bn, capacity = map(int, raw_input().split())
    bottles = map(int, raw_input().split())
    bottles.sort()
    for b in bottles:
        if b <= capacity:
            capacity -= b
            filled += 1
    print filled
