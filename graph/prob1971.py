# memory limit exceeded
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        conn = [ [0] * n for _ in range(n) ]
        
        for u, v in edges:
            conn[u][v] = 1
            conn[v][u] = 1
            
        visited = set()
        
        cur = [source]
        nxt = []
        visited.add(source)
        while True:
            while cur:
                v = cur.pop(0)
                if v == destination:
                    return True
                # visited.add(v)
                for j in range(n):
                    if conn[v][j] == 1 and j not in visited:
                        nxt.append(j)
                        visited.add(j)
            if not nxt:
                break
            else:
                cur = nxt
                nxt = []
                
        return False

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        from collections import defaultdict 
        
        conn = defaultdict(set)
        
        for u, v in edges:
            conn[u].add(v)
            conn[v].add(u)
            
        visited = set()
        
        cur = [source]
        nxt = []
        visited.add(source)
        while True:
            while cur:
                v = cur.pop(0)
                if v == destination:
                    return True
                for j in conn[v]:
                    if j not in visited:
                        nxt.append(j)
                        visited.add(j)
            if not nxt:
                break
            else:
                cur = nxt
                nxt = []
                
        return False
