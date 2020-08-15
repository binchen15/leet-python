# 678 Valid Parenthesis String

# Not working.  
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        if m == 0:
            return True
        if m == 1:
            return s == "*"

        if "*" not in set(s):
            return self.checkPure(s)

        for i, c in enumerate(s):
            if c == "*":
                if self.checkValidString(s[:i] + s[i+1:]) or \
                self.checkValidString(s[:i] + ")" + s[i+1:]) or \
                self.checkValidString(s[:i] + "(" + s[i+1:]):
                    return True
        return False

    def checkPure(self, s):
        stk = 0
        for c in s:
            if c == "(":
                stk += 1
            elif c == ")":
                stk -= 1
                if stk < 0:
                    return False
        return stk == 0

# 40%
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftwild = 0
        for c in s:   # all ) must be matched
            if c == ")":
                leftwild -= 1
                if leftwild < 0:
                    return False
            else:
                leftwild += 1

        # leftwild >= 0, but how to distinguish left/wild?

        left = 0
        for c in s:  #
            if c == "(":
                left += 1
            else:
                left = max(0, left-1)
        return left == 0

# similar solution.
# can not stack ")" because non-symmetry between left, right
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
        if left > 0:
            return False

        leftwild = 0
        for c in s:
            if c == ")":
                leftwild -= 1
                if leftwild < 0:
                    return False
            else:
                leftwild += 1

        return True
