# 541 Reverse String II

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ""
        k2 = k * 2
        m = len(s)

        n_2k = m // k2
        remainder = m % k2

        for i in range(n_2k):
            st = self.reverse(s[i*k2: i*k2+k]) + s[i*k2+k:i*k2+k2]
            ans += st

        if remainder:
            tail = s[n_2k*k2:]
            if remainder > k:
                last = self.reverse(tail[:k]) + tail[k:]
            else:
                last = self.reverse(tail)
            ans += last

        return ans

    def reverse(self, s):
        a = list(s)
        a.reverse()
        return "".join(a)

