# timeout 
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        arr = [ [0] * n for _ in range(m)]

        for a, b in ops:
            for r in range(a):
                for c in range(b):
                    arr[r][c] += 1


        mx = max(max(arr))

        c = 0

        for i in range(m):
            for j in range(n):
                if arr[i][j] == mx:
                    c += 1

        return c

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        xs = []
        ys = []
        for x, y in ops:
            xs.append(x)
            ys.append(y)
            
        if not xs:
            return m * n
        
        a = min(xs)
        b = min(ys)
        
        return a * b
