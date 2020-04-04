# 58 Length of Last Word

# use a for loop instead of map, filter
# for an early stop
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        m = len(words)
        if not m:
            return 0
        for i in range(m-1, -1, -1):
            if len(words[i]) > 0:
                return len(words[i])
        return 0
        
