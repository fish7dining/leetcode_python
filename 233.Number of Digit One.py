class Solution:
    # @param {integer} n
    # @return {integer}

    def go(self, x):
        if x=='0':
            return 0
        L = len(x)
        if L==1:
            return 1
        ans = 0
        first = int(x[0])
        ans += first*(2**(L-1)-1)
        if first > 1:
            ans += 10**(L-1)
        temp = self.go(x[1:])
        if first==1:
            ans += (temp+1+int(x[1:]))
        else:
            ans += temp
        return ans

    def countDigitOne(self, n):
        if n <= 0:
            return 0
        x = str(n)
        ans = self.go(x)
        return ans


a = Solution()
print a.countDigitOne(20)
print a.countDigitOne(13)
print a.countDigitOne(100)