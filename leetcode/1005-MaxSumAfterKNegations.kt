/**
 * 1005. Mazimize Sum Of Array After K Negations
 * https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/submissions/
 *
 **/
class Solution {
    
    fun largestSumAfterKNegations(A: IntArray, K: Int): Int {
        A.sort()
        var remainingNegations = K
        var index = 0

        //negate all numbers lower or equals than zero
        while (index < A.size && A[index] <= 0 && remainingNegations > 0) {
            A[index] *= -1
            remainingNegations--
            index++
        }

        if (remainingNegations > 0) {
            //no need to negate if the remaining negations is even
            if (remainingNegations % 2 != 0) {
                //negate the smallest number between the last negated and the first positive
                if (index > 0 && A[index] > A[index-1]) {
                    index--
                }
                A[index] *= -1
            }
        }

        return A.sum()
    }
}
