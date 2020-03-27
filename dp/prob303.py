# 303 Range Sum Query -Immutable

# 7% bad solution.
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return False
        dp = [False] * (N+1)  # assume Fail for all N numbers
        dp[1] = False
        dp[2] = True
        for n in range(3, N+1):
            for d in range(1, n//2+1):
                if n % d == 0:
                    if dp[n-d] == False:
                        dp[n] = True
                        break
        return dp[-1]

# 15% solution
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.hmap = {}
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i, j) in self.hmap:
            return self.hmap[(i,j)]
        else:
            ret = sum(self.nums[i:j+1])
            self.hmap[(i,j)] = ret
            return ret
        
# need a dp solution...
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [0] * len(nums)
        m = len(nums)
        if not m:
            return
        self.sums[0] = nums[0]
        for i in range(1, m):
            self.sums[i] = self.sums[i-1] + self.nums[i]
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]
        
