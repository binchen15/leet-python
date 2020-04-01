# 6 ZigZag Conversion

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] +s[1::2]
        
        l1 = numRows # inorder
        l2 = l1 - 2  # reverse
        
        m = len(s)
        data = []
        r = 0
        i = 0
        while i < m:
            if r & 1:  # odd
                t = s[i:i+l2]
                row = [""] + list(t[::-1]) + [""]
                l = len(row)
                if l < l1:
                    row = ([""] * (l1-l)) + row
                i  += l2
            else:
                t = s[i:i+l1]
                row = list(t)
                l = len(row)
                if l < l1:
                    row = row + ([""] * (l1-l))
                i += l1
            data.append(row)
            r += 1
        
        nr  = len(data)
        ans = ""
        for j in range(numRows):
            for i in range(nr):
                ans += data[i][j]
        return ans
                
