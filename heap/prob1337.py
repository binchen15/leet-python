class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        import heapq
        
        def helper(row):
            cnt = 0
            for v in row:
                if v == 1:
                    cnt += 1
                else:
                    return cnt
            return cnt
                
        m = len(mat)
        n = len(mat[0])
        
        obs = [ (helper(mat[i]), i) for i in range(m)]
        
        #print(obs)
        
        heapq.heapify(obs)
        
        ans = [ heapq.heappop(obs)[1] for i in range(k)]
        
        return ans
