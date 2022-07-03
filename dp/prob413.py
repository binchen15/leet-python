# 403 Number of arithmetic slices

# 65% solution
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        d = [ A[i] - A[i-1] for i in range(1, n)]
        i = 0
        j = 0
        cnts = [] # length of maximum arithmetic seqs.
        m = n - 1
        while i <= j and j < m:
            while j < m and d[j] == d[i]:
                j += 1
            if j == m:
                cnt = (m - 1) - i + 2
                if cnt >= 3:
                    cnts.append(cnt)
                break
            cnt = j - i + 1. 
            if cnt >= 3:
                cnts.append(cnt)
            i = j  # j is a new start 

        tot = 0 
        for cnt in cnts:
            tot += self.nas(cnt)
        return tot
            
    def nas(self, n):
        """return number of arithmetic sequence for [1,2,...,n]"""
        if n < 3:
            return 0
        return int(((n-2)*(n-1)) // 2)

# smart dp solution by some guy...
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0

        # dp[i] = number of arithmetic seq ends at A[i]
        dp = [0] * n
        # dp[0] = dp[1] = 0, clearly
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)        
        
        
if __name__ == "__main__":
	s = Solution()
	print(s.numberOfArithmeticSlices([1,2,3,8,9,10]))
	

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 2:
            return 0
        
        def helper(i):
            """start from nums[i] find the maximum j such as nums[i:j+1] 
            is arithemtic"""
            if i == n-1:
                return i
            j = i+1
            diff = nums[j] - nums[i]
            while j+1 < n and nums[j+1] - nums[j] == diff:
                j += 1
                
            return j
        
        def helper2(m):
            """for arithemtic seq of length m, find the total sub arithmetic"""
            return (m-1) * (m-2) //2
        
        ans = 0
        i = 0
        while i < n:
            j = helper(i)
            # print(j)
            if j == i:
                i += 1
            elif j - i < 2:
                i = j
            else:
                ans += helper2(j-i+1)
                i = j   # not j+1
                
        return ans

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 2:
            return 0

        dp = [0] * n

        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1]+ 1

        return sum(dp)
