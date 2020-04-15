# 817 Linked List Components

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        if not head or not G:
            return 0
        
        subset = set(G)
        cnt  = 0 # number of components
        prev = None  # previous node
        curr = head  # current node
        while curr:
            if curr.val not in G: # a break point
                if prev and prev.val in G:
                    cnt += 1
            prev = curr
            curr = curr.next
        if prev.val in G:
            cnt += 1
            
        return cnt
            
