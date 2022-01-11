class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        
        n = len(seq)
        cnt = 0
        depths = [0] * n
        
        for i, c in enumerate(seq):
            if c == "(":
                cnt += 1
                depths[i] = cnt
            else:
                depths[i] = cnt
                cnt -= 1
                
        return list(map(lambda x : x % 2, depths))
