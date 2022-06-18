# Split Two Strings to Make Palindrome

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        n = len(a)
        if self.isPalin(a, 0, n-1) or self.isPalin(b, 0, n-1):
            return True

        if a[0] == b[n-1]:
            l, r = 0, n-1
            while l+1 < r-1 and a[l+1] == b[r-1]:
                l += 1
                r -= 1
            if self.isPalin(a, l+1, r-1) or self.isPalin(b, l+1, r-1):
                return True

        if b[0] == a[n-1]:
            l, r = 0, n-1
            while l+1 < r-1 and b[l+1] == a[r-1]:
                l += 1
                r -= 1
            if self.isPalin(a, l+1, r-1) or self.isPalin(b, l+1, r-1):
                return True

        return False


    def isPalin(self, s, i, j):
        """is s[i:j+1] a palindrome?"""
        l, r = i, j
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
