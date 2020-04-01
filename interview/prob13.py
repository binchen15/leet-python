# 13 Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m == 0:
            return 0
       
        tot = 0
        # IV, IX, XL, XC, CD, CM
        d = {"I":1, "V":5, "X":10, "L":50,
             "C":100,  "D":500, "M":1000,
             "IV":4,   "IX":9,
             "XL":40,  "XC":90,
             "CD":400, "CM":900}
        i = 0 
        while i < m:
            c = s[i]
            if i < m-1:
                p = s[i:i+2]  # pair of chars
                if p in d: 
                    tot += d[p]
                    i   += 2
                else:
                    tot += d[c] 
                    i   += 1
            else:
                tot += d[c]
                i   += 1
        return tot
            
