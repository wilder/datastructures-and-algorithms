class Solution:
    # @param A : list of integers
    # @return an integer
    # [0, 1, 0, 1]
    def bulbs(self, A):
        counter = 0
        for i, _ in enumerate(A):
            if counter & 1:
                if A[i] == 0:
                    A[i] = 1
                else:
                    A[i] = 0
            
            if A[i] == 0:
                counter+=1
                A[i] = 1
            else:
                A[i] = 0
                
        return counter
