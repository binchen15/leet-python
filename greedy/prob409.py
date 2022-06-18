class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        odds = 0
        for key, val in freq.items():
            if val % 2 == 1:
                odds += 1
                
        if odds:
            ans = len(s) - odds +1
        else:
            ans = len(s)
            
        return ans
