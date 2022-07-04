# timelimit 42/44
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        ans = sys.maxsize

        def helper(path):
            ans = 0
            for i, j in enumerate(path):
                ans += triangle[i][j]

            return ans

        def walk(path, i):
            nonlocal ans
            if i == m:
                ans = min(ans, helper(path))
                return

            # quit early
            # if sum(path) >= ans:
            #    return
            if i == 0:
                walk([0], 1)
            else:
                walk(path + [path[-1]], i+1)
                walk(path + [path[-1]+1], i+1)

        walk([], 0)

        return ans

# still timelimit error. 42/44 passed
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        ans = sys.maxsize
         
        def walk(path, ps, i):
            nonlocal ans
            if i == m:
                ans = min(ans, ps)
                return
            
            # quit early
            # if sum(path) >= ans:
            #    return
            if i == 0:
                walk([0], ps + triangle[0][0], 1)
            else:
                walk(path + [path[-1]], ps + triangle[i][path[-1]],  i+1)
                walk(path + [path[-1]+1], ps + triangle[i][path[-1]+1],  i+1)
            
        walk([], 0,  0)
            
        return ans

# 43/44 passed
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        ans = sys.maxsize
        memo = {}
        
        def walk(path, ps, i):
            nonlocal ans
            if i == m:
                ans = min(ans, ps)
                return
            
            if i > 0:
                p = (i-1, path[-1])  # last point visited
                if p not in memo:
                    memo[p] = ps
                elif ps >= memo[p]:
                    return  # can not be cheaper
                else:
                    memo[p] = ps
                
            if i == 0:
                walk([0], ps + triangle[0][0], 1)
            else:
                walk(path + [path[-1]], ps + triangle[i][path[-1]],  i+1)
                walk(path + [path[-1]+1], ps + triangle[i][path[-1]+1],  i+1)
            
        walk([], 0,  0)
            
        return ans

# 60% DP solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)

        t = triangle

        dp = [[0] * m for _ in range(m)]
        dp[0][0] = t[0][0]
        for i in range(1, m):
            dp[i][0] = t[i][0] + dp[i-1][0]

        for i in range(1, m):
            for j in range(1, i+1):
                if j == i:
                    dp[i][j] = dp[i-1][j-1] + t[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + t[i][j]

        return min(dp[m-1])

# DP with O(N) memory
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)

        t = triangle

        dp = [0] * m
        dp[0] = triangle[0][0]
        for i in range(1, m):
            dp[i] = dp[i-1] + t[i][i]
            for j in range(i-1, 0, -1):
                dp[j] = min(dp[j-1], dp[j]) + t[i][j]
            dp[0] = dp[0] + t[i][0]


        return min(dp)
