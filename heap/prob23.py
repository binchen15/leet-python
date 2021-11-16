# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MyNode:
    def __init__(self, lnode):
        self.lnode = lnode
        
    def __eq__(self, other):
        return self.lnode.val == other.lnode.val
    
    def __lt__(self, other):
        return self.lnode.val < other.lnode.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        lists = filter(lambda x : x is not None, lists)
        if not lists:
            return None
        
        h = [ MyNode(lnode) for lnode in lists]
        heapq.heapify(h)

        head = ListNode()
        cur  = head
        
        while h:
            mynode = heapq.heappop(h)
            cur.next = mynode.lnode
            cur = cur.next
            if mynode.lnode.next:
                heapq.heappush(h, MyNode(mynode.lnode.next))
                
        return head.next
            
