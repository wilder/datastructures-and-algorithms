n = int(raw_input().strip())
from collections import defaultdict
contacts = defaultdict(int)
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    partial = ''
    if op == 'add':
        for s in contact:
            partial+=s
            contacts[partial]+=1
    else:
        print contacts[contact]
