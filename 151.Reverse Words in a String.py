class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        x = s.split(' ')
        xx = []
        for i in x:
            if i != '':
                xx.append(i)
        xx.reverse()
        return ' '.join(xx)



a = Solution()
print a.reverseWords(' the sky is  blue ')
print a.reverseWords('  ')