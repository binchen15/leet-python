# 438 Find all anagrams in a string

# used hashmap
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = len(s)
        n = len(p)
        if m < n:
            return []
        
        hmap = {}
        for c in p:
            hmap[c] = hmap.get(c, 0) + 1
           
        i = 0
        hmap2 = {}
        
        ans = []
        while i < m - n + 1: # i_max = m - n
            if i == 0: # init
                for c in s[:n]:
                    hmap2[c] = hmap2.get(c, 0) + 1
            else:
                c1 = s[i-1]   # to go
                c2 = s[i+n-1] # to add
                if hmap2[c1] > 1:
                    hmap2[c1] -= 1
                else:
                    del hmap2[c1]
                hmap2[c2] = hmap2.get(c2, 0) + 1   
            if hmap2 == hmap:
                ans.append(i)    
            i += 1
        
        return ans

