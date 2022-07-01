class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        if k == 1 or n <= 1:
            return sum(arr)
        
        dp = [0] * n
        
        # initialize the first k elements 
        for i in range(k):
            dp[i] = max(arr[:i+1]) * (i+1)
        
        for i in range(k, n):
            tmp = 0
            for j in range(1, k+1): # length of last segment
                tmp = max(tmp, dp[i-j] + max(arr[i-j+1:i+1]) * (j))
                
            dp[i] = tmp
            
        return dp[n-1]
