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
	
