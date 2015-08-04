class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        left = [nums[0]]
        right = [nums[-1]]
        ans = []
        L = len(nums)
        for i in range(1,L):
            left.append(left[-1]*nums[i])
        for i in range(L-2,-1,-1):
            right.append(right[-1]*nums[i])
        right.reverse()
        ans.append(right[1])
        for i in range(1,L-1):
            ans.append(left[i-1]*right[i+1])
        ans.append(left[-2])
        return ans




a = Solution()
a.productExceptSelf([1,2,3,4])