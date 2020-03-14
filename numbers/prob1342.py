class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        curr = num
        i    = 0
        while curr > 0:
            if curr & 1:
                curr -= 1
            else:
                curr //= 2
  				# curr = curr >> 1
            i += 1
        return i
