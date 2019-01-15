import kotlin.test.assertFalse
import kotlin.test.assertTrue

/**
 * This problem was asked by Microsoft.
 *
 * Given a 2D matrix of characters and a target word,
 * write a function that returns whether the word can be
 * found in the matrix by going left-to-right, or up-to-down.
 *
 * For example, given the following matrix:
 * [['F', 'A', 'C', 'I'],
 * ['O', 'B', 'Q', 'P'],
 * ['A', 'N', 'O', 'B'],
 * ['M', 'A', 'S', 'S']]
 *
 * and the target word 'FOAM', you should return true,
 * since it's the leftmost column.
 *
 * Similarly, given the target word 'MASS', you should return true, since it's the last row.
 *
 * Leetcode: https://leetcode.com/problems/word-search
 */
class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        for (rowIndex in 0 until board.size) {
            for (columnIndex in 0 until board[0].size) {
                val found = search(0, rowIndex, columnIndex, board, word)
                if (found) return true
            }
        }
        return false;
    }

    fun search(targetCharPos: Int, i: Int, j: Int, board: Array<CharArray>, word: String): Boolean {
        if(hasFoundWord(targetCharPos, word)) {
            return true
        }

        if (isOutOfBounds(i, j, board)) {
            return false
        }

        if (isVisited(i, j, board)) {
            println("Skipping Visited")
            return false
        }

        if (board[i][j] != word[targetCharPos]) {
            println("Skipping ${board[i][j]}")
            return false
        }

        println("Visiting: ${board[i][j]}")
        visit(i, j, board)

        val found = search(targetCharPos+1, i+1, j, board, word) || //down
            search(targetCharPos+1, i-1, j, board, word) || //up
            search(targetCharPos+1, i, j+1, board, word) || //right
            search(targetCharPos+1, i, j-1, board, word) //left

        if (!found) {
            unvisit(i, j, board, word[targetCharPos])
            println("Unvisiting: ${board[i][j]}")
        }

        return found

    }

    private fun unvisit(i: Int, j: Int, board: Array<CharArray>, oldChar: Char) {
        board[i][j] = oldChar
    }

    private fun visit(i: Int, j: Int, board: Array<CharArray>) {
        board[i][j] = '#'
    }

    private fun isVisited(i: Int, j: Int, board: Array<CharArray>) = board[i][j] == '#'

    private fun isOutOfBounds(i: Int, j: Int, board: Array<CharArray>) =
        i >= board.size || j >= board[0].size || i < 0 || j < 0

    private fun hasFoundWord(targetCharPos: Int, word: String) = targetCharPos >= word.length
}

fun main(args: Array<String>) {
    assertTrue {
        Solution()
            .exist(arrayOf(
                charArrayOf('A','B','C','E'),
                charArrayOf('S','F','C','S'),
                charArrayOf('A','D','E','E')
            ), "ABCCED")
    }

    assertTrue {
        Solution()
            .exist(arrayOf(
                charArrayOf('A','B','C','E'),
                charArrayOf('S','F','C','S'),
                charArrayOf('A','D','E','E')
            ), "SEE")
    }

    assertFalse {
        Solution()
            .exist(arrayOf(
                charArrayOf('A','B','C','E'),
                charArrayOf('S','F','C','S'),
                charArrayOf('A','D','E','E')
            ), "ABCB")
    }

    assertTrue {
        Solution()
            .exist(arrayOf(
                charArrayOf('A','B','C','E'),
                charArrayOf('S','F','C','S'),
                charArrayOf('A','D','E','E')
            ), "ADEE")
    }

    assertTrue {
        Solution()
            .exist(arrayOf(
                charArrayOf('A','B','C','E'),
                charArrayOf('S','F','C','S'),
                charArrayOf('A','D','E','E')
            ), "ASA")
    }
}
