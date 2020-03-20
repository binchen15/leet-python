# 131 Palindrome partitioning
#20%

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        m = len(s)
        results = []
        self.dfs(m, [], 0, s, results)
        return results
        

    def dfs(self, m, parts, ptr, s, results):
        """parts: list of substrings of s
           ptr: starting index for next palindrome"""
        if ptr == m:
            results.append(parts[:])
            return
        for ptr2 in range(ptr+1,m+1): # s[ptr:ptr2]
            if self.palindrome(s, ptr, ptr2):
                print(ptr,ptr2, s[ptr:ptr2])
                parts.append(s[ptr:ptr2])
                self.dfs(m, parts, ptr2, s, results)
                parts.pop()
                
    def palindrome(self, s, start, end): 
        """is s[start:end] palindrome?"""
        t = s[start:end]
        n = len(t)
        if n <= 1:
            return True
        l = n // 2 - 1    # l,h double pointer from center go outward
        if n & 1:  # odd   
            h = l + 2
        else:
            h = l + 1
        while l >= 0:
            if t[l] != t[h]:
                return False
            l -= 1
            h += 1
        return True
        

