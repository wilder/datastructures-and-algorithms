'''
Given an array of positive integers (excluding zero) and a target number,
detect wheter ther is a set of consecutive elements in the array that add
to the target.

Example: a = {1, 3, 5, 7, 9}
target 8
output = true ({3,5})
'''

def consecutive(a, target):
    if not a:
        return False
    
    i = 0
    while i < len(a)-1:
        tracksum = a[i]
        nums = [a[i]] 
        print 'eta'
        for j in a[i+1:]:
            if (tracksum + j) <= target:
                tracksum+=j
                nums.append(j)
            if tracksum == target:
                print 'found ', nums
                return True
        i+=1

a = [1, 3, 5, 7, 9]
target = 12

print consecutive(a, target)


