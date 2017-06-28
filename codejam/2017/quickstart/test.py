t = int(raw_input()) #case
for t in range (1, t+1):
    n = int(raw_input())
    print "Case #{}: {}".format(t, n %2 == 0)
