n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

swaps = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            swaps +=1

print 'Array is sorted in', swaps, 'swaps.'
print 'First Element:', a[0]
print 'Last Element:', a[-1]
