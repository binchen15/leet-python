# 78 Subsets

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        results = []
        mask = [True] * n
        for k in range(n+1):
            self.dfs(k,[],nums,mask,results)
        return results
        
    def dfs(self, k, parts, nums, mask, results):
        if len(parts) == k:
            results.append(parts[:])
            return
        for i, num in enumerate(nums):
            if mask[i] and (not parts or num>parts[-1]):
                mask[i] = False
                parts.append(num)
                self.dfs(k, parts, nums, mask, results)
                parts.pop()
                mask[i] = True


