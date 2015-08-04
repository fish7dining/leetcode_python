class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        L = len(nums)
        self.ans = []
        if L==0:
            return self.ans
        for i in range(0,L-k+1):
            a = nums[i]
            for j in range(i+1,i+k):
                a = max( a,nums[j] )
            self.ans.append(a)
        return self.ans


a = Solution()
b = [1,3,-1,-3,5,3,6,7]
b = []
a.maxSlidingWindow(b, 0)
