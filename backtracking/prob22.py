# 22 generate parenthesis

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        def bt(s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if left < n:
                bt(s+"(", left+1, right)
            if left > right:
                bt(s+")", left, right+1)

        bt("", 0, 0)

        return ans

# closure number solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        ans = []
        for c in range(n):
            for s1 in self.generateParenthesis(c):
                for s2 in self.generateParenthesis(n-c-1):
                    ans.append( f"({s1}){s2}")
        return ans
