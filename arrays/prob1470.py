# 1470 shuffle array 

# inplace solution
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        j = 1
        for i in range(n, 2*n-1):
            e = nums[i]
            del nums[i]
            nums.insert(j, e)
            j += 2
        return nums
        
