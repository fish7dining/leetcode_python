class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        jie = []
        for i in range(n):
            if i==0:
                jie.append(1)
            else:
                jie.append(jie[-1]*i)
        jie.reverse()

        temp = []
        for i in range(1,n+1):
            temp.append(i)
        ans = ''
        k -= 1
        for i in range(n):
            index = ( k / jie[i] )
            ans += str( temp[index] )
            temp.pop(index)
            k %= jie[i]
        return ans



a = Solution()
print a.getPermutation(4, 24)
