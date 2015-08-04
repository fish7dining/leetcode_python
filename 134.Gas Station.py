class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        N = len(gas)
        for i in range(N):
            oil = 0
            bingo = True
            for j in range(i,N):
                oil = oil + gas[j] - cost[j]
                if oil < 0:
                    bingo = False
                    break
            if bingo == True:
                for j in range(0,i):
                    oil = oil + gas[j] - cost[j]
                    if oil < 0:
                        bingo = False
                        break
            if bingo == True:
                return i
        return -1


a = Solution()
print a.canCompleteCircuit([2,4], [3,4])