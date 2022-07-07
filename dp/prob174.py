# 174. Dungeon Game

# 70% in speed
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """        
        m = len(dungeon)
        if not m:
            return 1
        n = len(dungeon[0])
        if not n:
            return 1

        dp = [ [0] * n  for _ in range(m)]

        tmp = dungeon[m-1][n-1]
        if tmp <= 0:
            dp[m-1][n-1] = 1 - tmp
        else:
            dp[m-1][n-1] = 1
            
        for j in range(n-2, -1, -1): # last row
            nxt = dp[m-1][j+1]
            cur = dungeon[m-1][j]
            dp[m-1][j] = max(1, nxt-cur)
            
        for i in range(m-2, -1, -1): # last column
            nxt = dp[i+1][n-1]
            cur = dungeon[i][n-1]
            dp[i][n-1] = max(1, nxt-cur)
            
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                nxt = min(dp[i][j+1], dp[i+1][j])
                cur = dungeon[i][j]
                dp[i][j] = max(1, nxt-cur)
                
        return dp[0][0]
        
# Backtrack TimeLimit Error
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m = len(dungeon)
        n = len(dungeon[0])
        
        self.low = -sys.maxsize
        
        def walk(i, j, health, record):
            
            health += dungeon[i][j]
            record = min(record, health)
            
            if (i, j) == (m-1, n-1):
                self.low = max(self.low, record)
                return

            if record < self.low: # not a good route
                return
            
            if i < m-1:
                walk(i+1, j, health, record)
            if j < n-1:
                walk(i, j+1, health, record)
                
        walk(0, 0, 0, 0)
        
        return abs(self.low)+1

# DP, bottom up, right to left.
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [ [1] * n for _ in range(m)]
        
        # if dungeon[m-1][n-1] < 0:
        #     dp[m-1][n-1] += -dungeon[m-1][n-1]
    
        dp[m-1][n-1] = max(1, 1-dungeon[m-1][n-1])
    
        for j in range(n-2,-1,-1):
            dp[m-1][j] = max(1, 1-dungeon[m-1][j], dp[m-1][j+1] - dungeon[m-1][j])
            
        for i in range(m-2,-1,-1):
            dp[i][n-1] = max(1, 1-dungeon[i][n-1], dp[i+1][n-1] - dungeon[i][n-1])
            
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(1, 1-dungeon[i][j], min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
                
        return dp[0][0]     
