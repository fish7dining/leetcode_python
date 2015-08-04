class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        L = len(s)
        if L==0:
            return 0
        a = []
        ans = -1
        for i in range(L):
            if s[i] not in a:
                a.append(s[i])
                ans = max( ans, len(a) )
            else:
                while s[i] in a:
                    a.pop(0)
                a.append(s[i])
                ans = max( ans, len(a) )
        return ans



a = Solution()
a.lengthOfLongestSubstring("abcabcbb")
a.lengthOfLongestSubstring("bbbbb")