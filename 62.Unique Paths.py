class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        dp = [[0]*105 for i in range(105)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    dp[1][1] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

a = Solution()
print a.uniquePaths(1, 10)