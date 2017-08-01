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
            #remove the first non-removed element
            s-=a[low]
            low+=1
            continue

        if s == target:
            print a[low:i]
            return True 
        
        s+=a[i]
        i+=1
    
    return False
        
a = [1, 3, 5, 7, 9]
target = 12

print consecutive(a, target)


