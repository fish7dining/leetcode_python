class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*(len(nums)+10)
        dp[0] = nums[0]
        dp[1] = max( nums[0], nums[1] )
        L = len(nums)
        for i in range(2,L):
            dp[i] = max( dp[i-2]+nums[i], dp[i-1] )
        return dp[L-1]

a = Solution()
print a.rob([1,2,3,4,5])