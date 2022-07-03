# stone game II (memoization)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        @lru_cache(maxsize=None)
        def helper(i, j, M):
            """deals with piles[i:j+1] with initial M"""
            m = j-i+1
            if 2 * M >= m:
                return sum(piles[i:j+1])
            ans = 0
            for x in range(1, 2*M+1):
                M2 = max(M, x)
                tmp = sum(piles[i:j+1]) - helper(i+x, j, M2)
                ans = max(ans, tmp)

            return ans

        return helper(0, n-1, 1)
