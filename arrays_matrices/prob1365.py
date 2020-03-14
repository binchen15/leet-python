# how many numbers smaller than current numbers

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        histo = [0] * 101
        for n in nums:
            histo[n] += 1
        csum = 0 # cumulative sum
        for i in range(101):
            prev = histo[i]
            histo[i] = csum
            csum += prev
        
        return [ histo[n] for n in nums]  
