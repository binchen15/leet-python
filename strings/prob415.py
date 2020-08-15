# 415 Add strings (as numbers)

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m1 = len(num1)
        m2 = len(num2)
        m = max(m1, m2)
        s1 = map(int, num1)
        s2 = map(int, num2)
        s1.reverse()   # inplace
        s2.reverse()
        if m1 < m:
            s1 += [0] * (m-m1)
        if m2 < m:
            s2 += [0] * (m-m2)

        ans = []
        es  = [0]
        for i in range(m):
            e, c  = self.addDigits(s1[i], s2[i], es[i])
            ans.append(c)
            es.append(e)
        if e > 0:
            ans.append(e)
        # ans.append(e)
        # if len(ans) > 1 and ans[-1] == 0:
        #    ans.pop()
        ans.reverse()
        ans = map(str, ans)
        return "".join(ans)

    def addDigits(self, a, b, e):
        c = a + b + e
        if c >= 10:
            return (c//10, c%10)
        else:
            return (0, c)

