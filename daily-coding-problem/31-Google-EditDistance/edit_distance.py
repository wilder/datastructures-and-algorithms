'''
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''
def editDistance(strA, strB):

    memo = {}

    for i in range(len(strA)+1):
        for j in range(len(strB)+1):

            # cost of inserting.
            if i == 0:
                memo[(i,j)] = j #number of letters that B has more than A at this position

            # cost of deleting
            elif j == 0:
                memo[(i,j)] = i

            # if not the first letters and last character of both strings are equal
            # keep the cost of the past
            elif strA[i-1] == strB[j-1]:
                memo[(i,j)] = memo[(i-1, j-1)]

            else:
                memo[(i,j)] = 1 + min(memo[(i-1, j)], #deletion
                        memo[(i-1,j-1)], #replace
                        memo[(i, j-1)]) #insertion
    return memo[(len(strA), len(strB))]

if __name__ == '__main__':
    print(editDistance('kitten', 'sitting'))
    print(editDistance('kitten', 'bitten'))
    print(editDistance('kitten', 'light'))
    print(editDistance('kitten', 'kittens'))
