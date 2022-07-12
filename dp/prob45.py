# 45 Jump Game II

# TLE
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if not m:
            return 0
        ub = float('inf')
        dp = [-1] * m # -1 means unreachable
        dp[0] = 0
        for i in range(1, m):
            mj = ub # minimum jumps
            for j in range(i):
                if dp[j] >= 0 and nums[j] >= i-j:
                    # j can be reached, and j can jump to i
                    mj = min(mj, dp[j] + 1)
            if mj < ub:
                dp[i] = mj
        return dp[m-1]

# BFS
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 1:
            return 0
        level   = collections.deque() # queue of (index, jumps)
        visited = set()
        level.append((0,0))
        visited.add(0)
        while level:
            i, l = level.popleft()
            if i + nums[i] >= m-1:
                return l + 1
			# for j in range(1, nums[i]+1): # this fails....
            for j in range(nums[i], 0, -1):
                if i+j not in visited:
                    level.append( (i+j, l+1))
                    visited.add(i+j)
       
# BFS 13% solution
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 1:
            return 0
        q = collections.deque() # queue of (index, jumps)
        visited = set()  # across all levels
        q.append(0)
        visited.add(0)
        l = 0
        while q:
            nq = collections.deque()
            while q:
                i = q.popleft()
                if i + nums[i] >= m-1:
                    return l + 1
                for j in range(nums[i], 0, -1):
                    if i+j not in visited:
                        nq.append( i+j)
                        visited.add(i+j)
            q = nq
            l += 1

class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return 0

        cur = [0]
        jumps = 0
        nxt = []
        seen = set([0])
        while True:
            while cur:
                i = cur.pop(0)
                if i == n-1:
                    return jumps
                if nums[i] > 0:
                    for d in range(1, nums[i]+1):
                        if i + d < n:
                            if (i+d) not in seen:
                                nxt.append(i+d)
                                seen.add(i+d)
                        else:
                            break
            if not nxt:
                return -1
            else:
                cur = nxt
                nxt = []
                jumps += 1

        return -1


#  greedy solution
# each step, find the best next step. only jump there
#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here

	    if n == 1:
	        return 0

	    cur = 0
	    jumps = 0

	    while cur < n-1:
	        if arr[cur] > 0:
	            span = arr[cur]
	            if cur + span >= n-1:
	                return jumps + 1
	            nxt = cur+1 # try to find best next jump
	            for j in range(cur+1, cur+span+1):
	                if j + arr[j] > nxt + arr[nxt]:
	                    nxt = j

	            cur = nxt
	            jumps += 1
	        else:
	            return -1

        return  -1
