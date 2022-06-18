class Solution:
    def minSwaps(self, s: str) -> int:
        
        left = 0
        cnts = 0
        
        for char in s:
            if char == "[":
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    cnts += 1
                    
        return (left // 2) +  (left % 2) 
