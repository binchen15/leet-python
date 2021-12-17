class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=len)

        from functools import reduce

        def common(s1, s2):
            """assume len(s1) <= len(s2)"""
            n1 = len(s1)
            n2 = len(s2)

            if n1 == 0 or n2 == 0:
                return ""

            i = 0
            while i < n1 and s2.startswith(s1[:i+1]):
                i += 1

            return s1[:i]

        return reduce(common, strs)
