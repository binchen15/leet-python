class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        n = len(s)
        m = len(goal)

        return n == m and goal in s + s

