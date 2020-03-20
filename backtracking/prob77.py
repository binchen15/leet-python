# 77 Combinations

# 5% solution. why so slow.... embarassing
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1,n+1))
        if k > n:
            return []
        if k == n:
            return [nums]
        combo = []
        mask  = [True] * n
        self.backtrack(n,k,[],nums,mask,combo)
        #ans = [ list(t) for t in combo ] # tuple to list
        return combo #ans
        
    def backtrack(self, n, k, parts, nums, mask, combo):
        """parts: the stack store the current pieces"""
        if len(parts) == k:
            #tmp = tuple(parts) # list to tuple
            combo.append(parts[:])  # override if already exists
            return
        for i, num in enumerate(nums):
            if mask[i] and (not parts or num > parts[-1]): # unvisited
                mask[i] = False
                parts.append(num)
                self.backtrack(n,k,parts,nums,mask,combo)
                parts.pop()
                mask[i] = True
                
