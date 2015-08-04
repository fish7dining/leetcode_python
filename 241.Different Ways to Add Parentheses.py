class Solution:
    # @param {string} input
    # @return {integer[]}

    def isOpe(self, x):
        if x=='+' or x=='-' or x=='*':
            return True
        return False

    def Get(self, input):
        L = len(input)
        ans = []
        for i in range(L):
            if self.isOpe(input[i])==True:
                ans.append(input[i])
            else:
                if len(ans)==0 or self.isOpe(ans[len(ans)-1])==True:
                    ans.append(input[i])
                else:
                    ans[len(ans)-1] += input[i]
        return ans

    def go(self, stack, a):
        if len(stack)==1 and a==[]:
            self.ans.append(int(stack[0]))
        #1
        if len(stack) > 1:
            stack2 = list(stack)
            a2 = list(a)
            y = int(stack2.pop())
            ops = stack2.pop()
            x = int(stack2.pop())
            if ops=='+':
                stack2.append(x+y)
            elif ops=='-':
                stack2.append(x-y)
            else:
                stack2.append(x*y)
            self.go(stack2, a2)
        #2
        if len(a)>1:
            stack3 = list(stack)
            a3 = list(a)
            stack3.append(a3[0])
            stack3.append(a3[1])
            x = a3.pop(0)
            y = a3.pop(0)
            self.go(stack3, a3)

    def diffWaysToCompute(self, input):
        a = self.Get(input)
        self.ans = []
        stack = [a[0]]
        a.pop(0)
        self.go(stack, a)
        return self.ans


a = Solution()
a.diffWaysToCompute("2-1-1")
a.diffWaysToCompute("2*3-4*5")