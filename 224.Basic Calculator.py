class Solution:
    # @param {string} s
    # @return {integer}

    def isOpe(self, x):
        if x == '+' or x == '-' or x == '(' or x == ')':
            return True
        return False

    def init(self, s):
        x2 = ''
        for i in s:
            if i != ' ':
                x2 += i
        L = len(x2)
        ans = []
        for i in range(L):
            if self.isOpe(x2[i])==True:
                ans.append(x2[i])
            else:
                if len(ans)==0 or self.isOpe(ans[-1])==True:
                    ans.append(x2[i])
                else:
                    ans[-1] += x2[i]
        return ans

    def calc1(self, x):
        if len(x) == 1:
            return int(x[0])

        if x[1] == '+':
            ans = int(x[0]) + int(x[2])
        else:
            ans = int(x[0]) - int(x[2])
        x.pop(0)
        x.pop(0)
        x.pop(0)
        L = len(x)
        for i in range(0,L,2):
            if x[i] == '+':
                ans += int(x[i+1])
            else:
                ans -= int(x[i+1])
        return ans


    def calculate(self, s):
        x = self.init(s)
        L = len(x)
        stack = []
        for i in range(L):
            if x[i] != ')':
                stack.append(x[i])
            else:
                ans = []
                t1 = stack.pop()
                while t1 != '(':
                    ans.append(t1)
                    t1 = stack.pop()
                ans.reverse()
                stack.append(self.calc1(ans))
        if len(stack) > 0:
            return self.calc1(stack)
        else:
            return stack[0]




a = Solution()
print a.calculate('2147483647')
print a.calculate('(1+(4+5+2) -3)+(  6+  8)')
