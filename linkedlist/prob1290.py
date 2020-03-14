class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        curr = head
        ans  = 0
        while curr:
            ans = (ans << 1) + curr.val
            curr = curr.next
        return ans
        

