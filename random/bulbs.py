def change_state(bulbs):
    for i, _ in enumerate(bulbs):
        if bulbs[i] == 1:
            bulbs[i] = 0
        else:
            bulbs[i] = 1

def bulbs(A):
    counter = 0
    for i, _ in enumerate(A):
         if A[i] == 0class Solution:
    # @param A : list of integers
    # @return an integer
    def change_state(self, bulbs):
        for b, _ in enumerate(bulbs):
            if bulbs[b] == 1:
                bulbs[b] = 0
            else:
                bulbs[b] = 1
        return bulbs
    
    def bulbs(self, A):
        if not A or not 0 in A:
            return 0
        counter = 0
        for i, _ in enumerate(A):
            if A[i] == 0:
                A[i:] = self.change_state(A[i:])
                counter+=1
        return counter:
             print 'before changing', A
             change_state(A[i:])
             counter+=1
             print 'changed', A
    return counter

a = [0, 1, 0, 1]
print bulbs(a)
