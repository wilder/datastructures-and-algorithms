'''
Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted 
from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, 
she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in 
non-decreasing order. Some examples of this are 8, 123, 555, and 224488. 

She decided to call these numbers tidy. Numbers that do not have this property, 
like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N.
 What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. 
Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing 
Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.
'''

l = [(pow(10, n) - 1) / 9 * 10 for n in range(2,18)]

def get_last_tidy(n):
	if n % 10 == 0:
		if n < 100:
			return n - 1
	if n < 10:
		return n
	if n in l:
		return n / 10 * 9
	for i in xrange(n, 0, -1):#nunca vai chegar a 0. Parara no 9
		if is_tidy(i):
			return i


def is_tidy(n):
	tidy = []
	if n < 10:
		return True
	tidy = map(int, str(n))
	for i in range(len(tidy)-1):
		if tidy[i] > tidy[i+1]:
			return False 
	return True

	'''123355 26647984959
		123354 99999999999'''


def test():
	assert is_tidy(5)
	assert is_tidy(567)
	assert is_tidy(129)
	assert is_tidy(99)
	assert is_tidy(132) == False
	assert is_tidy(510) == False
	assert is_tidy(250) == False
	assert get_last_tidy(1000) == 999, get_last_tidy(1000)
	assert get_last_tidy(132) == 129, get_last_tidy(132)
	assert get_last_tidy(7) == 7, get_last_tidy(7)
	assert get_last_tidy(111111111111111110) == 99999999999999999, get_last_tidy(111111111111111110)


def main():
	t = int(raw_input()) #case
	for t in range (1, t+1):
	    n = int(raw_input())
	    print "Case #{}: {}".format(t, get_last_tidy(n))

if __name__ == '__main__':
	main()
	#test()
	#print get_last_tidy(132)