# 39 Combination Sum

#60% in speed
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m = len(candidates)
        results = []
        self.backtrack([], candidates, target, results)
        return results
        
    def backtrack(self, parts, candidates, target, results):
        if target == 0:
            results.append(parts[:])
            return
        if target < 0:
            return 
        for i, n in enumerate(candidates):
            if (not parts or n >= parts[-1]) and \
               target - n >= 0: # non-decreasing
                parts.append(n)
                self.backtrack(parts, candidates, target-n, results)
                parts.pop()
        return
                
        
