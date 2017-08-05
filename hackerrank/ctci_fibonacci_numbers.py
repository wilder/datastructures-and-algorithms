from collections import defaultdict
d = defaultdict(int)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        if d[n-1] == 0:
            d[n-1] = fibonacci(n-1)

        if d[n-2] == 0:
            d[n-2] = fibonacci(n-2)
       
        d[n] = d[n-1] + d[n-2]

        return d[n]
    
n = int(raw_input())
print(fibonacci(n))
print d
