#!/bin/python

import sys

def can_pop(stk, x, s):
    return stk and (stk[-1]+s <= x)

def pick(stk, s, removed):
    #print 'removedb', removed
    #print 's',s
    last = stk.pop()
    s+=last
    removed+=1
    #print 'picked: ',last
    #print 'removed: ', removed
    #print 's',s
    return s, removed, last

def unpick(stk, s, removed, last):
    stk.append(last)
    s-=last
    if removed > 0:
        removed-=1
    return s, removed

def backtrack(stks, x, s, removed, possibilities):
    #print '------ init ------'
    #print 'removed', removed
    
    if (not stks[0] and not stks[1]) or ((stks[0] and s+stks[0][-1] > x) and (stks[1] and s+stks[1][-1] > x)):
        #TODO: append to results?
        #\print 'ue',s, '+', stks[0][-1], '=', s+stks[0][-1]
        #print 'ue',s, '+', stks[1][-1], '=', s+stks[1][-1]
        #print 'removed', removed
        possibilities.append(removed)
        #print '-----------------\n'
        return removed
    
    for stk in stks:
        if not can_pop(stk, x, s):
            continue
        #print 'will pick - removed:',removed
        s, removed, last = pick(stk, s, removed)
        removed = backtrack(stks, x, s, removed, possibilities)
        #print '------- again -----'
        #print 'removed ',removed
        s, removed = unpick(stk, s, removed, last)
    #TODO: figure out what to return here
    return 0
        
g = int(raw_input().strip())
for a0 in xrange(g):
    n,m,x = raw_input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    possibilities = []
    backtrack([a[::-1], b[::-1]], x, 0, 0, possibilities)
    #print possibilities
    print max(possibilities)
