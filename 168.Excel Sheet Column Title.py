class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        ans = ''
        while n >= 26:
            x = n % 26
            if x==0:
                ans = 'Z' + ans
            else:
                ans = chr(ord('A')+x-1) + ans
            n /= 26
        ans = chr(ord('A')+n-1) + ans
        return ans



a = Solution()
print a.convertToTitle(26)
print a.convertToTitle(27)
print a.convertToTitle(53)