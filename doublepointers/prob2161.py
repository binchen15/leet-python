# silly solution
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        n = len(nums)
        
        l1 = []
        l2 = []
        cnts = 0
        
        for n in nums:
            if n < pivot:
                l1.append(n)
            elif n == pivot:
                cnts += 1
            else:
                l2.append(n)
        
        return l1 + [pivot] * cnts + l2
