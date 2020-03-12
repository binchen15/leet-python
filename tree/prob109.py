# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method1: convert list to array...

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return self.arrayToBST(vals)
        
        
    def arrayToBST(self, vals):
        m = len(vals)
        if m == 1:
            root = TreeNode(vals[0])
            return root
        if m == 2:
            root = TreeNode(vals[1])
            left = TreeNode(vals[0])
            root.left = left
            return root
        mid = m // 2
        root = TreeNode(vals[mid])
        left  = self.arrayToBST(vals[:mid])
        right = self.arrayToBST(vals[mid+1:])
        root.left  = left
        root.right = right
        return root
        
