# 22 Generate Parentheses

# 8% solution
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        ans = []
        self.walk(n, "", ans)
        return ans
        
    def walk(self, n, s, ans):
        if len(s) == 2*n:
            if self.validate(s):
                ans.append(s)
            return
        if s.count(")") > s.count("(") or \
           s.count("(") > n or \
           s.count(")") > n:
            return
        for c in "()":
            self.walk(n, s+c, ans)
        
    def validate(self, s):
        """validate if string s of n pairs of () is well-formed """
        cnt = 0 # count of opening "("
        for c in s:
            if c == "(":
                cnt += 1
            else:
                if cnt <= 0:
                    return False
                else:
                    cnt -= 1
        return cnt == 0
        
# 60% solution
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        ans  = []
        cnts = [n,n] # number of "(" and ")"
        self.walk(cnts, "", ans)
        return ans
    
    def walk(self, cnts, s, ans):
        if cnts[0] == 0 and cnts[1] == 0:
            ans.append(s)
            return
        if cnts[1] < cnts[0]: # more ) used than (    
            return  # wrong case
        if cnts[1] == cnts[0]:
            cnts[0] -= 1
            self.walk(cnts, s+"(", ans)
            cnts[0] += 1
        else:
            if cnts[0] > 0:
                cnts[0] -= 1
                self.walk(cnts, s+"(", ans)
                cnts[0] += 1
            cnts[1] -= 1
            self.walk(cnts, s+")", ans)
            cnts[1] += 1
 
