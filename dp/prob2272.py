class Solution:
    def largestVariance(self, s: str) -> int:
        
        n = len(s)
        if n == 2:
            return 0
        
        def helper(c1, c2):
            ans = []
            for c in s:
                if c == c1:
                    ans.append(1)
                elif c == c2:
                    ans.append(-1)
            return ans
        
        def helper2(arr):
            
            m = len(arr)
            
            dp1 = [0] * m
            dp2 = [0] * m
            
            dp1[0] = arr[0]
            dp2[-1] = arr[-1]
            
            for i in range(1, m):
                dp1[i] = max(arr[i], arr[i] + dp1[i-1])
                
            
            for i in range(m-2, -1, -1):
                dp2[i] = max(arr[i], arr[i] + dp2[i+1])
                
            ans = -1
            for i in range(m):
                if arr[i] == -1:
                    ans = max(ans, dp1[i] + dp2[i] - arr[i])
                    
            return ans
                      
        ans = 0
        chars = string.ascii_lowercase
        t2 = set(s)
        
        for c1 in chars:
            for c2 in chars:
                if c1 == c2:
                    continue
                if c1 not in t2 or c2 not in t2:
                    continue
                arr = helper(c1, c2)
                var = helper2(arr)
                ans = max(ans, var)
                
        return ans
