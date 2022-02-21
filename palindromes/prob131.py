# 131 Palindrome partitioning
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

# 30%
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        ans = []
        
        def isPalindrome(s):
            n = len(s)
            if n <= 1:
                return True
            l, r = 0, n-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def walk(pieces, i):
            """i next index in s to start a new palindrome"""
            if i == n:
                ans.append(pieces)
                return
            
            for j in range(i+1, n+1):
                tmp = s[i:j]
                # if tmp == tmp[::-1]:
                if isPalindrome(tmp):
                    walk(pieces + [tmp], j)
                    
        walk([], 0)
        
        return ans
