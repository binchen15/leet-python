class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        m = len(s)
        if m <= 1:
            return
        for i in range(m // 2):
            s[i], s[m - 1 - i] = s[m - 1 - i], s[i] # swap
        return
