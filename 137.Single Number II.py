class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        nums.sort()
        L = len(nums)
        if L == 1:
            return nums[0]
        if nums[-1]!=nums[-2] or nums[-2]!=nums[-3]:
            if nums[-1]==nums[-2]:
                return nums[-3]
            else:
                return nums[-1]
        for i in range(0, L, 3):
            if nums[i]!=nums[i+1] or nums[i+1]!=nums[i+2]:
                if nums[i]==nums[i+1]:
                    return nums[i+2]
                else:
                    return nums[i]




a = Solution()
print a.singleNumber([1, 2, 3, 3, 2, 2, 3])