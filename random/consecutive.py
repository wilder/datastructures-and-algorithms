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
    
    #will be the index of the first non-removed element
    low = 0
    i = 0
    s = 0

    while i < len(a):
       
        if s > target:
            s-=a[low]
            low+=1
            continue
        

        if s == target:
            print a[low:i]
            return True 

        s+=a[i]
        i+=1
   
    return s == target

assert consecutive([3, 7, 9, 15, 2, 1, 5], 8)
assert consecutive([1, 3, 4, 7, 9, 15, 2, 5], 7)
assert consecutive([5, 7, 3, 1, 4], 4)
assert consecutive([1,2,3,4,5], 7)
assert consecutive([100, 2, 3, 1], 5)
assert consecutive([1, 3, 5, 7, 9], 12)
assert consecutive([1, 3, 7], 11)
assert consecutive([1, 3, 5, 7, 9], 8)
