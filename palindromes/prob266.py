class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            
        odd = False
        for key in counts:
            if counts[key] % 2 == 1:
                if odd:
                    return False
                else:
                    odd = True

        return True 
