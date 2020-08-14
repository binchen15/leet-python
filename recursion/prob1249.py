# 1249 Minimum Remove to Make Valid Parentheses

# not working with "))(("
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""

        stk = 0
        start = 0
        first = -1  # first left parentheis
        for i, c in enumerate(s):
            if c == "(":
                stk += 1
                if first < 0:
                    first = i
            elif c == ")":
                if stk > 0:
                    stk -= 1
                    if stk == 0:
                        ans += s[start:i+1]
                        start = i+1
                else:
                    ans += s[start:i]
                    start = i+1
        if stk == 0:
            return ans + s[start:]
        else:
            return s[:first] + self.minRemoveToMakeValid(s[first+1:])


# 5% ugly solution
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        if m == 0:
            return s
        if m == 1:
            if s == "(" or s == ")":
                return ""
            else:
                return s
        if "(" not in s and ")" not in s:
            return s

        stk = 0
        first = -1
        for i, c in enumerate(s):
            if c == "(":
                stk += 1
                if first < 0:
                    first = i
            elif c == ")":
                if stk == 0:
                    return  s[:i] + self.minRemoveToMakeValid(s[i+1:])
                if stk > 0:
                    stk -= 1
                    if stk == 0:
                        return s[:i+1] + self.minRemoveToMakeValid(s[i+1:])

        if stk > 0:
            return s[:first] + self.minRemoveToMakeValid(s[first+1:])

# 5% still
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        if m == 0:
            return s
        if m == 1:
            if s == "(" or s == ")":
                return ""
            else:
                return s
        #if "(" not in s and ")" not in s:
        #    return s

        stk = 0
        first = -1
        for i, c in enumerate(s):
            if c == "(":
                stk += 1
                if first < 0:
                    first = i
            elif c == ")":
                if stk == 0:
                    return  s[:i] + self.minRemoveToMakeValid(s[i+1:])
                if stk > 0:
                    stk -= 1
                    if stk == 0:
                        return s[:i+1] + self.minRemoveToMakeValid(s[i+1:])

        if stk > 0:
            return s[:first] + self.minRemoveToMakeValid(s[first+1:])
        else:
            return s

