# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()

if not s:
    print "not pangram"
else:
    s = s.replace(" ", "").lower()
    a = set()

    for i in s:
        a.add(i)
    
    if len(a) == 26:
        print 'pangram'
    else:
        print 'not pangram'
