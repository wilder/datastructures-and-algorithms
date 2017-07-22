def ransom_note(magazine, ransom):
    from collections import defaultdict
    d = defaultdict(int)
    for w in magazine:
        d[w] += 1
        
    for w in ransom:
        d[w] -= 1
        
    for _, value in d.iteritems():
        if value < 0:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer):
    print "Yes"
else:
    print "No"
