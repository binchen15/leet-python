class Solution:
    def minDeletions(self, s: str) -> int:
        
        from collections import Counter
        
        d = Counter(s)
        ans = 0
        
        while d and not self.isUnique(d):
            delta = self.helper(d)
            ans += delta
            
        return ans
    
    def isUnique(self, d):
        values = d.values()
        return len(set(values)) == len(values)
    
    
    def helper(self, d):
        """assume d is not empty, and handles the most frequent chars in d"""
        
        m = max(d.values())
        flag = True
        ans = 0
        
        e = {key: val for key, val in d.items() }
        
        for key, val in e.items():
            if val == m:
                if flag:
                    del d[key]
                    flag = False
                else:
                    if m == 1:
                        del d[key]
                    else:
                        d[key] = m-1     
                    ans += 1
                    
        return ans

class Solution:
    def minDeletions(self, s: str) -> int:

        from collections import Counter

        d = Counter(s)
        ans = 0

        while d and not self.isUnique(d):
            delta = self.helper(d)
            ans += delta

        return ans

    def isUnique(self, d):
        values = d.values()
        return len(set(values)) == len(values)


    def helper(self, d):
        """assume d is not empty, and handles the most frequent chars in d"""

        m = max(d.values())
        flag = True # for the first one with highest count, delete the key, others reduce the count by 1
        ans = 0

        items = list(d.items())
        for key, val in items:
            if val == m:
                if flag:
                    del d[key]
                    flag = False
                else:
                    if m == 1:
                        del d[key]
                    else:
                        d[key] = m-1
                    ans += 1

        return ans

