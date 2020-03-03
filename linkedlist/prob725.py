# partition linked list

# 57 percentile in speed

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if k == 1:
            return [root]
        if root == None:
            return [root] * k

        curr = root
        m    = 0       # length of list
        while curr != None:
            m   += 1
            curr = curr.next

        q, r = m // k, m % k
        ans = []  # store the list of heads
        #i = 1   # travaser the list again
        curr = root
        prev = None
        for p in range(k):
            if curr == None:
                ans.append(None)
                continue
            else:
                ans.append(curr)

            if p < r:
                n = q + 1
            else:
                n = q
            for _ in range(n):
                prev = curr
                curr = curr.next
            if prev:
                prev.next = None #  split the list

        return ans

