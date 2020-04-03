# 23 Merge k sorted lists

# Time Limit Error
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        m    = len(lists)
        if not m:
            return None
        curr = head

        currs = [ node for node in lists if node]
        while True:
            vals  = [ node.val for node in currs]
            mv  = float('inf')
            pos = -1
            for i, v in enumerate(vals):
                if v != None and v < mv:
                    mv  = v
                    pos = i
            if pos == -1:
                break  # end of all lists
            else:
                currs[pos] = currs[pos].next
                curr.val = mv
                currs = [ node for node in currs if node]
                if currs:
                    curr.next = ListNode()
                    curr = curr.next
        if head.val == None:
            return None
        return head
                
# 5% solution
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        m = len(lists)
        if not m:
            return None
        
        currs = [ node for node in lists if node]
        if not currs:
            return None
        head = ListNode(None)
        curr = head
        while currs:
            vals  = [ node.val for node in currs]
            mv  = float('inf')
            pos = -1
            for i, v in enumerate(vals):
                if v < mv:
                    mv  = v
                    pos = i
            if currs[pos].next:
                currs[pos] = currs[pos].next
            else:
                del currs[pos]  
            curr.val = mv
            if currs:
                curr.next = ListNode()
                curr = curr.next
            else:  
                break
        
        return head
                
# 90% fake solution
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        m = len(lists)
        if not m:
            return None
        vals = []
        for node in lists:
            curr = node
            while curr:
                vals.append(curr.val)
                curr = curr.next
        
        vals.sort()
        if not vals:
            return None
        head = ListNode(vals[0])
        curr = head
        for i in range(1, len(vals)):
            node = ListNode(vals[i])
            curr.next = node
            curr= curr.next
        
        return head
                
# 60% min-heap, priority queue based solution
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [n for n in lists if n]
        m = len(lists)
        if not m:
            return None
         
        hp   = [] # min heap of maximal size k
        # initialize the min heap
        for i in range(m):
            heapq.heappush(hp, (lists[i].val, i) ) # sort by the first entry
            lists[i] = lists[i].next
          
        head = ListNode()
        curr = head
        while hp:    
            val, j = heapq.heappop(hp)  
            curr.val = val
            if lists[j]: # not empty
                heapq.heappush(hp, (lists[j].val, j))
                lists[j] = lists[j].next
            if hp:
                node = ListNode()
                curr.next = node
                curr = curr.next
        return head
        
# divide and conquer    
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [n for n in lists if n]
        m = len(lists)
        if not m:
            return None
         
        return self.mergeLists(lists, 0, m-1)
        
    def mergeLists(self, lists, l, r): # [l, r] inclusive
        if l > r:
            return None
        if l == r:
            return lists[l]
        if l + 1 == r: # only two
            return self.mergeTwoLists(lists[l], lists[r])
        m = l + (r-l)//2
        a = self.mergeLists(lists, l,   m)
        b = self.mergeLists(lists, m+1, r)
        return self.mergeTwoLists(a, b)
               
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val > l2.val:
            l1, l2 = l2, l1   # switch them
        # l1 always has the smallest element
        #  make senses to merge whole l2 onto l1
        
        ptr1 = l1
        ptr2 = l2
        
        while ptr2 != None:
            while ptr1.next and ptr1.next.val <= ptr2.val:
                ptr1 = ptr1.next
            # dest.next first bigger, or None
            new  = ptr1.next   # memorize it
            new2 = ptr2.next
            ptr1.next = ptr2  # insert the node
            ptr2.next = new
            ptr2 = new2
            ptr1 = ptr1.next
            
        return l1
            
         
