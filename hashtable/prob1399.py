class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        
        def sumDigits(n):
            s = 0
            while n > 0:
                n, r = divmod(n, 10)
                s += r
            return s
        
        cnts = {}
        for i in range(1, n+1):
            t = sumDigits(i)
            cnts[t] = cnts.get(t, 0) + 1
            
        c2 = {}
        
        for k, v in cnts.items():
            c2[v] = c2.get(v, 0) + 1
            
        m = max(cnts.values())
        
        return c2[m]
