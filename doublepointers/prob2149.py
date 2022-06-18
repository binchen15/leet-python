class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * n
        pp, pn = 0, 1
        for v in nums:
            if v > 0:
                ans[pp] = v
                pp += 2
            else:
                ans[pn] = v
                pn += 2
                
        return ans
