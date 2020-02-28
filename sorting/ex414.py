# third "dinstinct" largest element in a list
# 
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(set(nums), reverse=True)
        if len(l) >= 3:
            return l[2]
        else:
            return l[0]

class Solution(object):
    """this use min heap, but it is atcually slower"""
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        s = set(nums)
        if len(s) < 3:
            return max(s)
        else:
            h = []
            for n in s:
                if len(h) < 3:
                    heapq.heappush(h, n)
                elif n > h[0]:
                    heapq.heapreplace(h, n)
            return h[0]
                    
        
