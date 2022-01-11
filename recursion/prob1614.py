class Solution:
    def maxDepth(self, s: str) -> int:
        
        pieces = self.partition(s)
        if not pieces:
            return 0
        n = len(pieces)
        if n == 1:
            l, r = pieces[0]
            return 1 + self.maxDepth(s[l+1:r])
        else:
            return 1 + max([self.maxDepth(s[l+1:r]) for (l, r) in pieces])
            
    
    def partition(self, s):
        ans = []
        if len(s) <= 1:  ## or "(" not in s:
            return ans
        
        n = len(s)
        
        i = 0
        cnt = 0
        tmp = []
        while i < n:
            if s[i] == "(":
                cnt += 1
                if cnt == 1:
                    tmp.append(i)   
            elif s[i] == ")":
                cnt -= 1
                if cnt == 0:
                    tmp.append(i)
                    ans.append(tmp)
                    tmp = []
            i += 1
        return ans
