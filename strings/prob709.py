class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join(map(self.tr, str))
    
    def tr(self, c):
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return chr(ord(c) + ord('a') - ord('A'))
        else:
            return c
         
