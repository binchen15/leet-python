# valid parenthesis via stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        if m == 0:
            return True
        if m % 2:  # odd number of chars
            return False
        
        stack = []
        d = {")" : "(",
             "]" : "[",
             "}" : "{" }
        for char in s:
            if char in d.values():
                stack.append(char) # push to stack
            else: #if char in d.keys():
                if not stack:
                    return False
                v = stack[-1]
                if v != d[char]:
                    return False
                else:
                    del stack[-1]
        if stack:
            return False
        else:
            return True
