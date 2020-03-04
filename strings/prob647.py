class Solution(object):
    """first attempt, over time limit"""
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m <= 1:
            return m
        tot = 0
        for i in range(m):
            for j in range(i+1,m+1):
                sub = s[i:j]
                if self.palindrome(sub):
                    tot += 1
        return tot
    
    def palindrome(self, sub):
        m = len(sub)
        if m == 1:
            return True
        
        for i in range(m // 2):
            if sub[i] != sub[m - 1 - i]:
                return False
        return True
                
class Solution(object):
    """recursion, time limt error again"""
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m <= 1:
            return m
        
        tot = 0
        for i in range(m):
            for j in range(i+1, m+1):
                if self.isPalindrome(s[i:j]):
                    tot += 1
        return tot
        
    def isPalindrome(self, s):
        m = len(s)
        if m == 0:
            return False
        elif m == 1:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            if m == 2:
                return True
            else:
                return self.isPalindrome(s[1:-1])        


class Solution(object):
    """method 3, with memoization, still time out"""
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m <= 1:
            return m

        self.memo = set()

        tot = 0
        for i in range(m):
            for j in range(i+1, m+1):
                if self.isPalindrome_memo(s, i, j):
                    tot += 1
        #print("memo", self.memo)
        return tot


    def isPalindrome_memo(self, s, i, j):
        """is s[i:j] a palindrome? """
        if (i,j) in self.memo:
            #print(i,j)
            return True
        m = len(s)
        if not (i >= 0 and j <= m):
            return False
        if i == j:
            return False
        if i + 1 == j:  # singleton
            self.memo.add((i,j))
            return True
        if s[i] != s[j-1]:
            return False
        else:
            if i + 2 == j:
                self.memo.add((i,j))
                #print(i,j)
                return True
            else:
                return self.isPalindrome_memo(s, i+1, j-1)

class Solution(object):
    """method 4. still time limit error"""

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m <= 1:
            return m

        self.memo = set()

        tot = 0
        for i in range(m):
            for j in range(i+1, m+1):
                if self.isPalindrome_memo(s, i, j):
                    tot += 1
        print("memo", self.memo)
        return tot


    def isPalindrome_memo(self, s, i, j):
        """is s[i:j] a palindrome? """
        if (i,j) in self.memo:
            #print(i,j)
            return True

        m = len(s)
        if not (i >= 0 and j <= m):
            return False
        if i == j:
            return False
        if i + 1 == j:  # singleton
            self.memo.add((i,j))
            return True
        if s[i] != s[j-1]:
            return False
        else:
            if i + 2 == j:
                self.memo.add((i,j))
                #print(i,j)
                return True
            else:
                ans = self.isPalindrome_internal(s[i+1:j-1])
                if ans:
                    self.memo.add((i,j))
                    self.memo.add((i+1,j-1))
                return ans

    def isPalindrome_internal(self, s):
        if not s:
            return False
        m = len(s)
        if m == 0:
            return False
        if m == 1:
            return True
        for i in range(m // 2):
            if s[i] != s[m - 1 - i]:
                return False
        return True

# inside out. this solution works

class Solution(object):
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot = 0
        m   = len(s)
        for i in range(m):
            tot += self.expandPalindrome(s, i, i)
            tot += self.expandPalindrome(s, i, i+1)
        return tot
    
    def expandPalindrome(self, s, i, j):
        tot = 0
        m   = len(s)
        while i >= 0 and j < m and i <= j and s[i] == s[j]:
            tot += 1
            i -= 1
            j += 1
        return tot

class Solution(object):
    """inside out. this works!"""
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot = 0
        m   = len(s)
        for i in range(m):
            tot += self.expandPalindrome(s, i, i)
            tot += self.expandPalindrome(s, i, i+1)
        return tot
    
    def expandPalindrome(self, s, i, j):
        tot = 0
        m   = len(s)
        while i >= 0 and j < m and i <= j and s[i] == s[j]:
            tot += 1
            i -= 1
            j += 1
        return tot

