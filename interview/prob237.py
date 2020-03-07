# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        while curr.next != None:
            curr.val = curr.next.val
            if curr.next.next == None:
                curr.next = None
                break
            curr = curr.next
        return
        
