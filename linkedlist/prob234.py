# palindrome number

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = []
        if head == None or head.next == None:
            return True

        curr = head
        while curr != None:
            d.append(curr.val)
            curr = curr.next

        m = len(d)
        for i in range(m // 2):
            if d[i] != d[m-i-1]:
                return False
        return True

