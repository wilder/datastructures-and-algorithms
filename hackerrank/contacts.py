def add(contact):
    partial = ''
    for s in contact:
        partial += s
        contacts[partial]+=1
        
def find(partial):
    return contacts[partial]
    
from collections import defaultdict
contacts = defaultdict(int)

n = int(raw_input())
for _ in range(n):
    op, arg = raw_input().split()
    if op == 'add':
        add(arg)
    else:
        print find(arg)
