# TLE. 85/87 cases passed
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        @lru_cache(maxsize=None)
        def walk(i, j):
            ans = [1]
            for l, w in envelopes:
                if l > i and w > j:
                    ans.append( 1 + walk(l, w))
            return max(ans)

        ans = 1
        for x, y in envelopes:
            ans = max(ans, walk(x, y))

        return ans

# same. 
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        @lru_cache(maxsize=None)
        def walk(i, j):
            ans = 1
            for l, w in envelopes:
                if l > i and w > j:
                    ans = max(ans, 1 + walk(l, w))
            return ans

        ans = 1
        for x, y in envelopes:
            ans = max(ans, walk(x, y))

        return ans

# LIS solution.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        e = envelopes
        e.sort(key = lambda x : (x[0], -x[1]))

        res = []

        for _, h in e:
            if not res or h > res[-1]:
                res.append(h)
            else:
                i = bisect.bisect_left(res, h)
                res[i] = h

        return len(res)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # sort by increasing widthm decreasing height
        e = envelopes
        e.sort(key = lambda x : (x[0], -x[1]))
        res = []

        # LIS for the height
        # the width must be different if height goes up
        n = len(e)
        dp = [1] * n
        for i in range(1, n):
            v = e[i][1]
            arr = []
            for j in range(i):
                if e[j][1] < v:
                    arr.append(dp[j])

            if arr:
                dp[i] = 1 + max(arr)

        return max(dp)
