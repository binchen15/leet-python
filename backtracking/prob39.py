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
                
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        
        ans = set()
        
        def walk(comb, val):
            if val == 0:
                ans.add(tuple(sorted(comb)))
            if val < 0:
                return
            
            for candidate in candidates:
                if candidate > val:
                    break
                if comb and candidate < comb[-1]:
                    continue
                walk(comb + [candidate], val-candidate)
                
        walk([], target)
                    
        return list(ans)

