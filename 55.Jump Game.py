class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        L = len(nums)
        pd = [False] * (L+10)
        pd[L-1] = True
        for i in range(L-2,-1,-1):
            for j in range(i,min(i+nums[i],L-1)+1):
                if pd[j] == True:
                    pd[i] = True
                    break
        return pd[0]



a = Solution()
print a.canJump([1,3,1,1,4])
print a.canJump([3,2,1,0,4])