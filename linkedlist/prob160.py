# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """time out"""
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        A = headA
        while A != None:
            B = headB
            while B != None:
                if A == B:
                    return A
                else:
                    B = B.next
            A = A.next
        return None
       

class Solution(object):
    """50% solution"""
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        a = []
        b = []
        A = headA
        while A != None:
            a.append(A)
            A = A.next
        B = headB
        while B != None:
            b.append(B)
            B = B.next
            
        la = len(a)
        lb = len(b)
        l  = min(la, lb)
        sect = None
        for i in range(l):
            if a[la-1-i] == b[lb-1-i]:
                sect = a[la-1-i] 
            else:
                break
        return sect
           
        
class Solution(object):
    """70% solutino"""
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        a = headA
        b = headB
        while a != b:
            if a != None :
                a = a.next   # traverse A first
            else:   
                a = headB    # switch to B
            if b != None:    # traverse B first
                b = b.next
            else:            # switch to A
                b = headA
        # when exit, both = None, or the intersection point        
        return a 
                 
