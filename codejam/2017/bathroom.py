#!/usr/bin/python

from heapq import *


def solve(n, k,q):

	ls = 0
	lr = 0
	while(k>=0):

		ref = n >> 1
		if(n%2!=0):
			ls = ref
			lr = ref

		else:
			ls = ref -1
			lr = ref
			

	 	k = k-1

	return ls,lr



if __name__ == '__main__':
	t = int(raw_input())

	for i in xrange(1, t + 1):

		n, k = [int(s) for s in raw_input().split(" ")] 

		if(k>n or n==k):
			result = 0
			result2 = 0
		else:
			q = []
	  		result,result2 = solve(n,k,q)

	  	y = str(max(result,result2))
	  	x = str(i)
	  	z = str(min(result,result2))

	  	print "Case #{}: {} {}".format(x,y,z)