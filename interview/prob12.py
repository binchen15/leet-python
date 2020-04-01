# 12 Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        b1  = num % 10
        if b1: # not zero
            if b1 < 4:
                t = "".join(["I"]*b1)
            elif b1 == 4:
                t = "IV"
            elif b1 == 5:
                t = "V"
            elif b1 == 9:
                t = "IX"
            else:  # 6...8
                t = "V" + "".join(["I"]*(b1-5))
            ans = t + ans 
            
        num = num // 10
        if not num:
            return ans
        b1  = num % 10
        if b1: # not zero
            if b1 < 4:
                t = "".join(["X"]*b1)
            elif b1 == 4:
                t = "XL"
            elif b1 == 5:
                t = "L"
            elif b1 == 9:
                t = "XC"
            else:  # 6...8
                t = "L" + "".join(["X"]*(b1-5))
            ans = t + ans
            
        num = num // 10
        if not num:
            return ans
        b1 = num % 10
        if b1: # not zero
            if b1 < 4:
                t = "".join(["C"]*b1)
            elif b1 == 4:
                t = "CD"
            elif b1 == 5:
                t = "D"
            elif b1 == 9:
                t = "CM"
            else:  # 6...8
                t = "D" + "".join(["C"]*(b1-5))
            ans = t + ans
            
        num = num // 10
        if not num:
            return ans
        b1 = num % 10
        t = "".join(["M"]*b1)
        ans = t + ans
        
        return ans
