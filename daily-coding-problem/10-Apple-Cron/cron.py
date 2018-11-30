'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import time
def scheduler(function, milliseconds):
    time.sleep(milliseconds/1000)
    function


def sum(a, b):
    print('sum = {0}'.format(a + b))
    return a + b

scheduler(sum(4,5), 1000)
