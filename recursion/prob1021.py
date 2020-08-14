# 1021 Remove Outermost parentheses

# recursion. slow 6% solution...
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) in (0, 2):   # must be even by nature
            return ""

        stk = 0   # stack
        for i, c in enumerate(S):
            if c == "(":
                stk += 1
            else:  # c == ")"
                stk -= 1
                if stk == 0:  # close the first "("
                    part1 = S[1:i]
                    return part1 + self.removeOuterParentheses(S[i+1:])

# 80% solution. non-recursive
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) in (0, 2):   # must be even by nature
            return ""

        ans = ""
        start = 0  # starting index of current block
        stk = 0    # stack
        for i, c in enumerate(S):
            if c == "(":
                stk += 1
            else:  # c == ")"
                stk -= 1
                if stk == 0:  # close the starting "("
                    part1 = S[start+1:i]
                    ans += part1
                    start = i+1
        return ans

