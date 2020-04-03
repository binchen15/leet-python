# 25 Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        
        lists = self.partition(head, k)
        m     = len(lists)
        pieces = []
        for i in range(m): 
            myhead, reverse = lists[i]
            if reverse:
                new_head = self.reverseList(myhead)
            else:
                new_head = myhead
            pieces.append(new_head)
        for i in range(m-1):
            lists[i][0].next = pieces[i+1]
            
        return pieces[0]
                
    def partition(self, head, k):
        """partition list in k-group"""
        ans = []
        if not head:
            return ans
        curr = head
        cnt  = 0
        while curr:
            cnt += 1   
            if cnt % k == 0: # terminate here
                tmp = curr.next
                curr.next = None
                ans.append([head, True])
                head = tmp
                curr = head
                cnt  = 0 # might be None
            else:
                curr = curr.next
        if head:
            ans.append([head,False])
        return ans
                    
    def reverseList(self, head):
        """reverse a linked list"""
        if not head:
            return None
        if not head.next:
            return head

        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
        
