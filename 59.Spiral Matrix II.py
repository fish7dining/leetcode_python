class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n==0:
            return []

        dp = [([0]*105) for i in range(105)]
        for i in range(n+2):
            dp[0][i] = 999
            dp[n+1][i] = 999
            dp[i][0] = 999
            dp[i][n+1] = 999
        x = 1
        y = 1
        N = 1
        while 1:
            if N > n*n:
                break
            #right
            while dp[x][y] == 0:
                dp[x][y] = N
                y += 1
                N += 1
            y -= 1
            x += 1
            #down
            while dp[x][y] == 0:
                dp[x][y] = N
                x += 1
                N += 1
            x -= 1
            y -= 1
            #left
            while dp[x][y] == 0:
                dp[x][y] = N
                y -= 1
                N += 1
            y += 1
            x -= 1
            #up
            while dp[x][y] == 0:
                dp[x][y] = N
                x -= 1
                N += 1
            x += 1
            y += 1
        ans = []
        for i in range(1,n+1):
            t = []
            for j in range(1,n+1):
                t.append(dp[i][j])
            ans.append(t)
        return ans


a = Solution()
print a.generateMatrix(9)