class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        n = 0
        A = bin(A + 2**32)
        for i in str(A):
            if i == '1':
                n+=1
        return n-1
