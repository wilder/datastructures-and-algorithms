'''
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column is set to 0.
'''


'''
solution 1:
    Time Complexity: O(N*M)
    Space Complexity: O(N+M)
'''
from collections import defaultdict
def setTo0(mat):
    rows_with_zero = defaultdict(int)
    columns_with_zero = defaultdict(int)

    for i, _ in enumerate(mat):
        for j, _ in enumerate(mat[i]):
            if mat[i][j] == 0:
                rows_with_zero[i] = 1
                columns_with_zero[j] = 1


    for i, _ in enumerate(mat):
	for j, _ in enumerate(mat[i]):
        	if rows_with_zero[i] == 1 or columns_with_zero[j] == 1:
        		mat[i][j] = 0

    return mat

if __name__ == '__main__':
    print setTo0([[1,1,1,1,0],
                 [0,0,1,1,1],
                 [0,1,1,1,1],
                 [1,1,1,1,1]])

    print setTo0([[0,0,0,0],[1,1,1,1],[1,1,1,1]])
