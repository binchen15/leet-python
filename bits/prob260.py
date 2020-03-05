class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # x xor y for the two single numbers
        xy = 0
        for n in nums:
            xy ^= n

        # this fit bit where x differs from y
        diff = xy & -xy
        
        ans = [0, 0]
        for n in nums:
            """pairs goes to same bucket, the 
						two sigle numbers go to different buckets"""
            if n & diff == 0:
                ans[0] ^= n
            else:
                ans[1] ^= n
        return ans
            
