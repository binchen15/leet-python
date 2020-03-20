# 46 Permutations of list of integers

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m    = len(nums)
        mask = [True] * m # True means unvisited yet
        if m == 1:
            return [nums]
        
        results = []
        self.dfs(m, [], nums, mask, results)
        return results
        
    def dfs(self, m, parts, nums, mask, results):
        if len(parts) == m:
            results.append(parts[:])
            # results.append(parts) # this will not work.
            return
        for i, n in enumerate(nums):
            if mask[i]:
                parts.append(n)
                mask[i] = False
                self.dfs(m, parts, nums, mask, results)
                mask[i] = True
                parts.pop()
        return
            
 
