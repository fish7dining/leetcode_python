class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        ans = {}
        ress = 0
        for i in nums:
            if i not in ans:
                ans[i] = 777
                ress += 1
        return ress

a = Solution()
print a.removeDuplicates([1,1,2])
