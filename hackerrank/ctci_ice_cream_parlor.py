t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    
    from collections import defaultdict

    d = defaultdict(int)
    for i, cost in enumerate(a):
        if d[m-cost] != 0:
            print d[m-cost], i+1
        else:
            d[cost] = i+1
