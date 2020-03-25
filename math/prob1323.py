# 1323 maximum 69 number

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = str(num)
        return int(digits.replace('6', '9', 1))


