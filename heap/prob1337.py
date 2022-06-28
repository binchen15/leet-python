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

# Bisecting to count ones
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
        
        
        def helper2(row):
            
            n = len(row)
            l, r = 0, n-1
            if row[r] == 1:
                return n
            if row[l] == 0:
                return 0
            
            while l < r:
                if r - l == 1:
                    if row[r] == 1:
                        return r + 1
                    else:
                        return l + 1
                else:
                    m = (l+r) // 2
                    if row[m] == 1:
                        l = m
                    else:
                        r = m - 1
                        
            return l + 1
            
                    
        m = len(mat)
        n = len(mat[0])
        
        obs = [ (helper2(mat[i]), i) for i in range(m)]
        
        #print(obs)
        
        heapq.heapify(obs)
        
        ans = [ heapq.heappop(obs)[1] for i in range(k)]
        
        return ans
