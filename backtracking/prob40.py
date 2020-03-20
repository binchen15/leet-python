# 40. Combination Sum II

# 20% in speed
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m = len(candidates)
        mask = [True] * m   # True , unvisited 
        results = []
        uniq    = set()
        self.backtrack([], candidates, target, results, mask, uniq)
        return results
    
    def backtrack(self, parts, candidates, target, results, mask, uniq):
        if target == 0:
            if tuple(parts) not in uniq:
                results.append(parts[:])
                uniq.add(tuple(parts))
            return
        if target < 0:
            return
        for i, n in enumerate(candidates):
            if (not parts or n >= parts[-1]) and \
                mask[i] and target - n >= 0:
                parts.append(n)
                mask[i] = False
                self.backtrack(parts, candidates, target-n, results,mask, uniq)
                mask[i] = True
                parts.pop()
        
