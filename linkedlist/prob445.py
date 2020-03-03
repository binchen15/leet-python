# represent integers as singly linked list
# add two numbers, and return the result as a list
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.list_to_number(l1)
        n2 = self.list_to_number(l2)
        n3 = n1 + n2
        text = str(n3)
        head = ListNode(int(text[0]))
        #curr = head
        prev = head
        for c in text[1:]:
            node = ListNode(int(c))
            prev.next = node
            prev = node
        return head
        
    def list_to_number(self, l):
        """convert list to number"""
        if l == None:
            return 0
        curr = l
        num  = 0
        while curr != None:
            num = num*10 + curr.val
            curr = curr.next
        return num
