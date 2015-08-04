class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        a = ['1']
        for i in range(1,n):
            x = list(a[i-1])
            c = 1
            letter = x[0]
            ans = ''
            for i in range(1,len(x)):
                if x[i] == letter:
                    c += 1
                    continue
                else:
                    ans += ( str(c) + letter )
                    c = 1
                    letter = x[i]
            ans += ( str(c) + letter )
            a.append(ans)
        return a[n-1]


a = Solution()
print a.countAndSay(3)