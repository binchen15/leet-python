# 560 Subarray Sum Equals K

# brute force
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m  = len(nums)
        # dp[i][j] partial sum of nums[i:j+1]
        dp = [ [10**8] * m for _ in range(m) ]
        for i in range(m):
            dp[i][i] =  nums[i]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + nums[j]
            
        for i in range(1, m):
            prev = nums[i-1]
            for j in range(i+1, m):
                dp[i][j] = dp[i-1][j] - prev

        cnt = 0
        for i in range(m):
            for j in range(m):
                if dp[i][j] == k:
                    cnt += 1
        return cnt
            
# prefix sum still TLE
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m  = len(nums)
        ps = [0] * m
        ps[0] = nums[0]
        for i in range(1, m):
            ps[i] = ps[i-1] + nums[i]
        
        cnt = 0
        for i in range(m):
            for j in range(i, m): # nums[i:j+1]
                if (i-1 >= 0  and ps[j]-ps[i-1] == k) or \
                   (i == 0 and ps[j] == k) :
                    cnt += 1
        return cnt
            
# use hashmap O(n) solution
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m  = len(nums)
        ps = [0] * (m+1) # padding by 1 unit
        hmap = {}
        cnt = 0
        for i in range(1, m+1):
            tmp   = ps[i-1] + nums[i-1]
            ps[i] = tmp
            if tmp == k:
                cnt += 1
            cnt += hmap.get(tmp-k, 0)
            hmap[tmp] = hmap.get(tmp, 0) + 1
        return cnt
        
