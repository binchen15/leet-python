class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
         
        tot  = 0
        flag = 0
        for val in d.values():
            tot += (val // 2) * 2
            if val % 2 == 1:
                flag = 1
        if flag:
            tot += 1
        return tot
            
       
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
         
        tot  = 0
        flag = True
        for val in d.values():
            if val % 2 == 0:
                tot += val
            else:
                if flag:
                    tot += val
                    flag = False
                else:
                    tot += val - 1
                
        return tot
            
        
