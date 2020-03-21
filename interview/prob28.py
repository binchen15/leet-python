# 28. Implement strStr()

# 5% solution
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        ptr = 0
        m   = len(needle)
        n   = len(haystack)
        while ptr < n and haystack[ptr:ptr+m] != needle:
            ptr += 1
        if ptr == n:
            return -1
        else:
            return ptr

# 37% solution
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        n   = len(haystack)
        m   = len(needle)
        if m > n:
            return -1

        curr = 0
        while curr + m -1 < n:
            while curr + m -1 < n and haystack[curr] != needle[0]:
                curr += 1
            if curr + m -1 == n:
                return -1
            match = True
            for j in range(1, m):
                if haystack[curr+j] != needle[j]:
                    match = False
                    break
            if match:
                return curr
            else:
                curr += 1
        return -1



