class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        a = abs(x)
        y = list(str(a))
        y.reverse()
        res = ''
        for i in y:
            res += i

        if x < 0:
            res = -int(res)
        else:
            res = int(res)
        if res > 2147483647 or res < -2147483648:
            return 0
        else:
            return res


a = Solution()
print a.reverse(12300)
a.reverse(-123)