/**
 * 807. Max Increase to Keep City Skyline
 * https://leetcode.com/problems/max-increase-to-keep-city-skyline/
 */
class MaxIncreaseKeepingSkyline {

    fun maxIncreaseKeepingSkyline(grid: Array<IntArray>): Int {
        val maxPerLineAndColumn: Pair<List<Int>, List<Int>> = getMaxPerLineAndColumn(grid)
        val lineMax = maxPerLineAndColumn.first
        val columnMax = maxPerLineAndColumn.second

        var increasedHeightSum = 0

        grid.forEachIndexed { lineIndex, line ->
            line.forEachIndexed { columnIndex, currentHeight ->
                val increasedHeight = Math.min(lineMax[lineIndex], columnMax[columnIndex])
                increasedHeightSum += increasedHeight - currentHeight
            }
        }

        return increasedHeightSum
    }

    private fun getMaxPerLineAndColumn(grid: Array<IntArray>): Pair<List<Int>, List<Int>> {
        val lineMax = MutableList(grid.size) {-1}
        val columnMax = MutableList(grid.size) {-1}

        grid.forEachIndexed{ lineIndex, line ->
            line.forEachIndexed{ columnIndex, height ->
                lineMax[lineIndex] = Math.max(lineMax[lineIndex], height)
                columnMax[columnIndex] = Math.max(columnMax[columnIndex], height)
            }
        }

        return Pair(lineMax, columnMax)
    }


}
