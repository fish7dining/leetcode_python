# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        a = ""
        b = ""
        while l1.next != None:
            a += str(l1.val)
        a += str(l1.val)
        while l2.next != None:
            b += str(l2.val)
        b += str(l2.val)
        ans = list(int(a)+int(b))
        res = ListNode(ans[0])
        pp = res
        ans.pop(0)
        while len(ans) > 0:
            pp.next = ListNode(ans[0])
            pp = pp.next
            ans.pop(0)
        return res



