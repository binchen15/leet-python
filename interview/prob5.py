# 5 Longest Palindrome Substring

# 50% solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        if m <= 1:
            return s
        d = [0] * m
        
        loc = 0  # which index store the longest palindrome
        for i in range(m):
            d[i] = self.palindrome(m, s, i)
            if d[i] > d[loc]:
                loc = i
        size = d[loc]
        half = size // 2
        if size & 1:
            return s[loc-half:loc+half+1]
        else:
            return s[loc-half+1:loc+half+1]
            
    def palindrome(self, m, s, i):
        """length of palindrome centered at i"""
        odd = 1
        j   = 1
        while 0 <= i-j and \
              i+j < m and \
            s[i-j] == s[i+j]:
            odd += 2
            j   += 1
                    
        even = 0
        j    = 0
        while 0 <= i-j and \
            i+1+j < m and \
            s[i-j] == s[i+1+j]:
            even += 2
            j    += 1
            
        return max(odd, even)
    

