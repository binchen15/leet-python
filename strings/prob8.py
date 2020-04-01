# 8 String to Integer

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        m = len(str)
        if m == 0:
            return 0
        
        i = 0
        while i < m and str[i] == " ":
            i += 1
        if i == m:    # string with only white spaces
            return 0 
        c = str[i]    # starting char
        if c not in "+-0123456789":
            return 0
        j = i + 1
        while j < m and str[j] in "0123456789":
            j += 1
        if j - i == 1 and c not in "0123456789":
            return 0
        # now at least one real digit
        if c in "+-":
            k = i+1
        else:
            k = i
        tot = 0
        for d in str[k:j]:
            tot = tot * 10 + int(d)
        if c != "-":
            result =  tot
        else:
            result = -tot
            
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31 
        return result


