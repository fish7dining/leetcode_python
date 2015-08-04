class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        a = list(nums)
        L = len(nums)
        for i in range(L):
            a.pop(0)
            if target-nums[i] in a:
                x = i+1
                y = nums.index(target-nums[i], i+1,L)+1
                return [x, y]

a = Solution()
a.twoSum([2, 7, 11, 15], 9)