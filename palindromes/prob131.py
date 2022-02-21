class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        ans = []
        
        def walk(pieces, i):
            """i next index in s to start a new palindrome"""
            if i == n:
                ans.append(pieces)
                return
            
            for j in range(i+1, n+1):
                tmp = s[i:j]
                if tmp == tmp[::-1]:
                    walk(pieces + [tmp], j)
                    
        walk([], 0)
        
        return ans
