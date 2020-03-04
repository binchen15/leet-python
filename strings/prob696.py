class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m   = len(s)
        cnt = 0
        for i in range(m-1):
            if s[i] == s[i+1]:
                continue
            else:
                cnt += self.expand(s, i)
        return cnt
        
    def expand(self, s, i):
        m = len(s)
        l = i
        r = i + 1
        #if s[l] == s[r]:
        #   return 0
        cnt = 1
        while l - 1 >= 0 and \
              r + 1 < m  and \
              s[l-1] == s[l] and \
              s[r+1] == s[r] :
            cnt += 1
            l   -= 1
            r   += 1
        return cnt
        
        
