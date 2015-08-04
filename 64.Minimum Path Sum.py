class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        dp = [[99999999]*5000]*5000
        row = len(grid)
        column = len(grid[0])
        for i in range(0,row):
            for j in range(0,column):
                if i==0 and j==0:
                    dp[i+1][j+1] = grid[i][j]
                else:
                    dp[i+1][j+1] = min( dp[i][j+1], dp[i+1][j] ) + grid[i][j]
        return dp[row][column]


a = Solution()
print a.minPathSum([[1,2],[1,1]])