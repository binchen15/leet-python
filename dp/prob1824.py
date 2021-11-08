# 1824 Minimu side jump

class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        n = len(obstacles) - 1

        memo = [[0] * (n+1) for _ in range(3)]
        for i in range(1, n):
            if obstacles[i] != 0:
                memo[obstacles[i] - 1][i] = -1
        memo[0][0] = 1
        memo[2][0] = 1

        for c in range(1, n+1):
            for r in range(3):
                if memo[r][c] == -1:
                    continue
                candidates = []
                left = (r - 1) % 3
                right = (r + 1) % 3

                if memo[r][c-1] != -1:
                    candidates.append(memo[r][c-1])
                    for side in [left, right]:
                        if memo[side][c-1] != -1:
                            candidates.append(memo[side][c-1] + 1)
                else:
                    for side in [left, right]:
                        if memo[side][c-1] == -1:
                            continue
                        if memo[side][c] == -1:
                            candidates.append(memo[side][c-1] + 2)
                        else:
                            candidates.append(memo[side][c-1] + 1)
                memo[r][c] = min(candidates)

        return min([memo[r][n] for r in range(3)])
