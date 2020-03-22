# parlindome for singly linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """time limit exceeded error """    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        m = self.get_length(head)
        i = 0
        curr = head
        while i < m // 2:
            mirror = self.get_mirror_node(curr, m, i)
            if curr.val == mirror.val:
                i += 1
                curr = curr.next
            else:
                return False
        return True
                 
    def get_length(self, head):
        m    = 0
        curr = head
        while curr:
            m += 1
            curr = curr.next
        return m
        
    def get_mirror_node(self, curr, m, i):
        # given index i of current node , find mirror node
        if i > m - 1:
            return None
        j = m - 2*i - 1
        node = curr
        while j > 0:
            node = node.next
            j -= 1
        return node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        
               
