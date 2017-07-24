import sys
n = int(raw_input())
stack = []
max_stack = []
maxelem = -sys.maxsize
for i in range(n):
    q = map(int, raw_input().split())
    if q[0] == 1:
        elem = q[1]
        stack.append(elem)
        if maxelem <= elem:
            max_stack.append(maxelem)
            maxelem = elem
    elif q[0] == 2:
        elem = stack.pop()
        if elem == maxelem:
            if max_stack:
                maxelem = max_stack.pop()
    else:
        print maxelem
