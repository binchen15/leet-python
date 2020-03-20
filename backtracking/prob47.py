# 47 Permutations II (with duplicates)

# used a set to avoid duplciated permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m == 1:
            return [nums]
        mask = [True] * m
        results = []
        uniq    = set()
        self.dfs(m, [], nums, mask, results, uniq)
        return results
        
    def dfs(self, m, parts, nums, mask, results, uniq):
        if len(parts) == m:
            if tuple(parts) not in uniq:
                results.append(parts[:])
                uniq.add(tuple(parts))
            return
        for i, n in enumerate(nums):
            if mask[i]:
                parts.append(nums[i])
                mask[i] = False
                self.dfs(m, parts, nums, mask, results, uniq)
                parts.pop()
                mask[i] = True
                
