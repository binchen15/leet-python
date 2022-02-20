class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        memo = [ [0] * (n+1) for _ in range(2) ]

        for i in range(1, n+1):
            memo[0][i] = i
            
        for i in range(1, n+1):
            # building with i floors, aim at memo[1][i]
            
            arr = []
            for j in range(1, i+1):
                "drop the first egg at j-th floor"
                
                # egg broke
                n1 = memo[0][j-1]
                # egg not break
                n2 = memo[1][i-j]
                
                tmp = 1 + max(n1, n2)
                arr.append(tmp)
            
            memo[1][i] = min(arr)
            
        return memo[1][n]
