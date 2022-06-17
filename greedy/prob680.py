# 7% solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        
        def helper(i, j):
            if j - i <= 1:
                return True
            if s[i] == s[j]:
                return helper(i+1, j-1)
            
            # try remove i, or j
            if testPalin(i+1,j) or testPalin(i,j-1):
                return True
            else:
                return False
                
        def testPalin(i, j):
            l, r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        return helper(0, n-1)

# 45% solution
class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)

        def testPalin(i, j):
            l, r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, n-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if testPalin(l+1, r) or testPalin(l,r-1):
                    return True
                else:
                    return False

        return True

