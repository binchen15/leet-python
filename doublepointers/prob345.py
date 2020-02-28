class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        m = len(s)
        j = m - 1
        l = list(s)
        v = set("aeiouAEIOU")
        while i < j:
            while l[i] not in v and i + 1 < m:
                i += 1
            while l[j] not in v and j  > 0:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
                i += 1 
                j -= 1
 
        return "".join(l)
                
