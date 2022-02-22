class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        n = len(s)
        ans = 0    
        lc, rc = 0, 0
    
        start, end = 0, 1  # s[start:end]
        while end < n:
            if s[start] == "L":
                lc += 1
            else:
                rc += 1
            while lc != rc:
                if s[end] == "L":
                    lc += 1
                else:
                    rc += 1
                end += 1
            ans += 1
            start = end
            end = start + 1
            lc = 0
            rc = 0
            
        return ans
