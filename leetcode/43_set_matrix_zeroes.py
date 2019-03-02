'''
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/submissions/
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        protectedFirstRow = False
        protectedFirstColumn = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
                    if i == 0:
                        protectedFirstRow = True
                    
                    if j == 0:
                        protectedFirstColumn = True
                        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if protectedFirstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if protectedFirstColumn:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
