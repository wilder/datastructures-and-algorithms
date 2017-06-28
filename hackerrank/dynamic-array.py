seqList = []
lastAnswer = 0

def init_seq(seq, n):
    for i in range(n):
        seq.append([])

def execQuery(query, seqList, n, lastAnswer):
    q = query.split()
    queryType, x, y = int(q[0]), int(q[1]), int(q[2])
    index = ((x ^ lastAnswer) % n)
    try:
        seq = seqList[index]
    except:
        return lastAnswer
    if(queryType == 1):
        seq.append(y)
    else:
        lastAnswer = seq[y % len(seq)]
        print lastAnswer
    return lastAnswer
        
    

#Reading the number of sequences and the number of queries
n, q = map(int, raw_input().split())
init_seq(seqList, n)

for i in range(q):
    lastAnswer = execQuery(raw_input(), seqList, n, lastAnswer)
