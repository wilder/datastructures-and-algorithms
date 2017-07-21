import sys

bpairs = {
    "(":")",
    "[":"]",
    "{":"}"
}

def isValid(s):
    stk = []
    for b in s:
        if b in "{[(":
            stk.append(b)
        else:
            if not stk or b != bpairs[stk.pop()]:
                return False
    return not stk

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    if isValid(s):
        print "YES"
    else:
        print "NO"
