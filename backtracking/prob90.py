# Subsets II

# slow though. used extra set for uniqueness. Need improve
# 5% in speed
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """   
        m = len(nums)
        mask = [True] * m
        results = []
        uniq = set()
        
        def backtrack(k,parts):
            if len(parts) == k:
                tmp = tuple(parts)
                if tmp not in uniq:
                    results.append(parts[:])
                    uniq.add(tmp)
            for i, n in enumerate(nums):
                if mask[i] and (not parts or n >= parts[-1]):
                    parts.append(n)
                    mask[i] = False
                    backtrack(k, parts)
                    parts.pop()
                    mask[i] = True
        for k in range(m+1):
            backtrack(k, [])
        return results
    

