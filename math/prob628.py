class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 3:
            return nums[0] * nums[1] * nums[2]
        
        nums.sort()
        
        if nums[0] >= 0:
            return nums[-1] * nums[-2] * nums[-3]
        
        if nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]
        
        if nums[1] <= 0:
            return max(nums[-1] * nums[-2] * nums[-3],
                       nums[-1] * nums[0] * nums[1]
                      )
        else:
            return nums[-1] * nums[-2] * nums[-3]

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if nums[0] >= 0 or nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]
        
        # nums[0] < 0 and nums[-1] > 0
        
        return max(nums[0] * nums[1] * nums[-1], nums[-1]*nums[-2]*nums[-3])
