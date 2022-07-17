# https://practice.geeksforgeeks.org/problems/410d51d667ab93f2219b15126f001f32e8bb029e/1?page=2&category[]=Greedy&sortBy=submissions
#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # code here

        intervals = []
        for i in range(n):
            x = gallery[i]
            if x >= 0:
                lb, ub = max(0, i-x), min(i+x, n-1)
                intervals.append( [lb, ub] )


        if not intervals:
            return -1

        intervals.sort(key = lambda x : [x[0], -x[1]])

        # print(intervals)

        # sanity check
        if intervals[0][0] > 0:
            return -1

        chosen =[ intervals[0] ]

        def helper(i):
            """start from index i find the next sprinkler"""
            lb = chosen[-1][1] # the right most position covered already
            if intervals[i][0] > lb + 1:     # must cover lb+1
                return -1      # gap can not be covered, will fail
            ans, ub = i, intervals[i][1]
            for j in range(i+1, len(intervals)):
                a, b = intervals[j]
                if a > lb + 1:
                    break
                if b > ub:  # find a better one
                    ans, ub = j, b
            if ub < lb + 1: # no progress made at all
                return -1
            return ans  # at least cover lb+1.

        i = 1 # to find next sprinkler to choose
        while i < len(intervals) and chosen[-1][1] < n-1:
            j = helper(i)
            if j == -1:
                return -1
            chosen.append(intervals[j])
            i = j+1

        if chosen[-1][1] < n-1:
            return -1
        else:
            return len(chosen)
