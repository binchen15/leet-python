# prob. 17 Letter combinations of phone number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {}
        d['2'] = ("a", "b", "c")
        d['3'] = ("d", "e", "f")
        d['4'] = ("g", "h", "i")
        d['5'] = ("j", "k", "l")
        d['6'] = ("m", "n", "o")
        d['7'] = ("p", "q", "r", "s")
        d['8'] = ("t", "u", "v")
        d['9'] = ("w", "x", "y", "z")
        
        m = len(digits)
        if m == 0:
            return []
        if m == 1:
            return list(d[digits])
        first  = self.letterCombinations(digits[0])
        remain = self.letterCombinations(digits[1:])
        ans = []
        for c in first:
            for sub in remain:
                ans.append(c + sub)
        return ans 
        

