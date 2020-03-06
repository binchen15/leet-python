class Solution(object):
    """10% solution... hmm."""
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for n in range(1, num+1):
            cnt = 0
            while n > 0:
                bit = n & 1
                if bit:
                    cnt += 1
                n = n >> 1
            ans.append(cnt)
        return ans
              
class Solution(object):
    """90% dynamic programming...
		    ans[i] = ans[i >> 1]  + (i & 1)
		"""
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0] * (num+1)
        for i in range(1, num+1):
            ans[i] = ans[i >> 1]  + (i & 1)
        return ans
