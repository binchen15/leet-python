#sort
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        
        return (nums[0]-1) * (nums[1]-1)

# heap
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        import heapq
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)

        a = -heapq.heappop(nums)
        b = -heapq.heappop(nums)
        
        return (a-1)*(b-1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        m1, m2 = 0, 0
        for v in nums:
            if v > m1:
                m2 = m1
                m1 = v
            elif v > m2:
                m2 = v
                
        return (m1-1)*(m2-1)
