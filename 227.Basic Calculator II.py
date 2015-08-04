class Solution:
    # @param {string} s
    # @return {integer}

    def isOpe(self, x):
        if x=='+' or x=='-' or x=='*' or x=='/':
            return True
        return False

    def init(self, s):
        a1 = s.split(' ')
        a2 = []
        for i in a1:
            if i != '':
                a2.append(i)
        x2 = ''
        for i in a2:
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

    def go(self, x):
        if len(x) == 1:
            return int(x[0])
        xx = []
        index = 9999999999
        if '*' in x:
            index = x.index('*')
        if '/' in x:
            index = min( index, x.index('/') )
        if index != 9999:
            for i in range(index-1):
                xx.append(x[i])
            if x[index] == '*':
                xx.append( int(x[index-1]) * int(x[index+1]) )
            else:
                xx.append( int(x[index-1]) / int(x[index+1]) )
            for i in range(index+2,len(x)):
                xx.append(x[i])
            return self.go(xx)

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
        return self.go(x)



a = Solution()
print a.calculate('1 +   2+  4 / 3')