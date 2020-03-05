class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = False   # number of 1 found
        if num == 0:
            return False
        
        cnt = 0   # position of the 1 bit
        while num > 0:
            bit = num & 1
            if bit:
                if flag:
                    return False
                flag = True
                if cnt % 2 != 0:
                    return False
            num = num >> 1
            cnt += 1
        return flag and cnt % 2 == 1
                
        
