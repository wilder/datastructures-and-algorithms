n = int(raw_input())

smap = {}
setlist = set()
l = []

#reading data
for i in range(n):
    elem = raw_input()
    #set used to initialize the dict
    setlist.add(elem)
    l.append(elem)

#init dict
for a in setlist:
    smap[a] = 0
    
#indexing values
for i in l:
    smap[i] = smap[i]+1
    
#querying
qnum = int(raw_input())
for i in range(qnum):
    try:
        query = raw_input()
        val = smap[query]
        print val
    except:
        print 0


