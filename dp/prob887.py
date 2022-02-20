# both time out error

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        memo = [[0] * (n+1) for _ in range(k)]

        for i in range(1, n+1):
            memo[0][i] = i
            
        for r in range(1, k):
            # case with r eggs in total
            
            for i in range(1, n+1):
                # try to fill in memo[r][i], r eggs and i floors
                
                arr = []
                for j in range(1, i+1):
                    # which floor to drop the first egg? j
                    
                    # egg breaks
                    n1 = memo[r-1][j-1]
                    # egg not breaks
                    n2 = memo[r][i-j]
                    
                    tmp = 1 + max(n1, n2)
                    
                    arr.append(tmp)
                
                memo[r][i] = min(arr)
                
        return memo[k-1][n]

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        memo = [[0] * (n+1) for _ in range(k)]

        for i in range(1, n+1):
            memo[0][i] = i
            
        for r in range(1, k):
            # case with r eggs in total
            
            for i in range(1, n+1):
                # try to fill in memo[r][i], r eggs and i floors
                
                ans = sys.maxsize
                
                for j in range(1, i+1):
                    # which floor to drop the first egg? j
                    
                    # egg breaks
                    n1 = memo[r-1][j-1]
                    # egg not breaks
                    n2 = memo[r][i-j]
                    
                    tmp = 1 + max(n1, n2)
                    
                    ans = min(ans, tmp)
                
                memo[r][i] = ans
                
        return memo[k-1][n]
