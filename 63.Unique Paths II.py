class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp = [[0]*105 for i in range(105)]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1 and obstacleGrid[0][0]==0:
                    dp[1][1] = 1
                else:
                    if obstacleGrid[i-1][j-1] == 1:
                        dp[i][j] = 0
                    else:
                        if obstacleGrid[i-2][j-1] == 0:
                            dp[i][j] = dp[i-1][j]
                        if obstacleGrid[i-1][j-2] == 0:
                            dp[i][j] += dp[i][j-1]
        return dp[m][n]



