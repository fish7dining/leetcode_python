class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        L = len(s)
        ans = []
        for i in range(L):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                ans.append(s[i]);
            else:
                if s[i]==')':
                    if len(ans)==0 or ans.pop()!='(':
                        return False
                elif s[i]==']':
                    if len(ans)==0 or ans.pop()!='[':
                        return False
                else:
                    if len(ans)==0 or ans.pop()!='{':
                        return False
        if len(ans) != 0:
            return False
        return True

a = Solution()
print a.isValid('()[]{[]}}')