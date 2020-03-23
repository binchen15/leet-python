# 1002 Find Common Characters

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        counts = []
        for s in A:
            tmp = [0] * 26
            for c in s:
                tmp[ord(c)-ord('a')] += 1
            counts.append(tmp)
        
        # minimum occurence counts of each char.
        mc = [0] * 26
        for i in range(26):
            tmp = min([ row[i] for row in counts])
            mc[i] = tmp
        ans = []
        for i, c in enumerate(mc):
            ans += [ chr(i+ord('a'))] * c
        return ans
            
            
        
