/*
 * 695. Max Area of Island
 * https://leetcode.com/problems/max-area-of-island/
 */

class MaxAreaOfIsland {
    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        var max = 0
        
        for (i in 0 until grid.size) {
            for (j in 0 until grid[i].size) {   
                if (grid[i][j] != 0) {
                    max = Math.max(max, dfs(grid, i, j))   
                }
            }
        }   
        
        return max
    }
    
    fun dfs(grid: Array<IntArray>, i: Int, j: Int): Int {
        if (i >= 0 && i < grid.size && j >= 0 && j < grid[0].size &&
                grid[i][j] != 0) {
            
            //mark as visited
            grid[i][j] = 0
            
            return 1 +
                dfs(grid, i, j + 1) +
                dfs(grid, i, j - 1) +
                dfs(grid, i + 1, j) +
                dfs(grid, i - 1, j) 
        }
        
        return 0
    }
    
    
}
