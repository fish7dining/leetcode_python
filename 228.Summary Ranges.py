class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ans = []
        p1 = 0
        p2 = 0
        L = len(nums)
        if L==0:
            return []
        for i in range(1,L):
            if nums[i]==nums[i-1]+1:
                p2 = i
            else:
                if p1==p2:
                    ans.append("%d"%nums[p1])
                else:
                    ans.append("%d->%d"%(nums[p1], nums[p2]))
                p1 = i
                p2 = i
        if p1==p2:
            ans.append("%d"%nums[p1])
        else:
            ans.append("%d->%d"%(nums[p1], nums[p2]))
        return ans

a = Solution()
print a.summaryRanges([-2,-1,0,1,2,4,5,7])