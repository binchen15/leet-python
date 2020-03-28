# 416 Partition Equal Subset Sum

# attempt 1
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False
        m = s // 2
        n  = len(nums)
        dp = [ [0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                v = nums[i-1]
                if v <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-v]+v)
                if j == m and dp[i][j] == m:
                    return True
        return False

# attempt 2
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False
        m = s // 2
        n  = len(nums)
        dp =  [0] * (m+1) 
        
        for i in range(1, n+1):
            for j in range(m, 0, -1):
                v = nums[i-1]
                if v <= j:
                    dp[j] = max(dp[j], dp[j-v]+v)
                if j == m and dp[j] == m:
                    return True
        return False
            
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False
        m = s // 2
        n  = len(nums)
        dp =  [0] * (m+1) 
        
        for i in range(1, n+1):
            v = nums[i-1]
            for j in range(m, v-1, -1):
                dp[j] = max(dp[j], dp[j-v]+v)
                if j == m and dp[j] == m:
                    return True
        return False


# definition of dp[i][j]:Boolean
# can we get the sum j using candidates up to nums[:i]
# if dp[i-1][j] already True, sure true, if not,
# can we get  j - nums[i] from nums[:i-1].
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False
        m  = s // 2
        n  = len(nums)
        dp =  [False] * (m+1)
        dp[0] = True 
        
        for i in range(1, n+1):
            v = nums[i-1]
            for j in range(m, v-1, -1):
                # dp[i-1][j] || dp[i-1][j-v]
                dp[j] = dp[j] or dp[j-v]
                if j == m and dp[j]:
                    return True
        return False
            
        
