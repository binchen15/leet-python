# 216 Combination Sum III

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = list(range(1,10))
        m    = 9  # len(nums)
        mask = [True] * m
        results = []
        self.backtrack(k,[],nums,n,results,mask)
        return results
        
    def backtrack(self, k, parts, nums, target, results, mask):
        if len(parts) == k or target <= 0:
            if len(parts) == k and target == 0:
                results.append(parts[:])
            return
        for i, n in enumerate(nums):
            if mask[i] and (not parts or n > parts[-1]) and \
               target - n >= 0:
                mask[i] = False
                parts.append(n)
                self.backtrack(k, parts, nums, target-n, results, mask)
                parts.pop()
                mask[i] = True
                
