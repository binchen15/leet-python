# 65 valid numbers

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        try:
            float(s)
            return True
        except:
            return False
