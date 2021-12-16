class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1
        ans = [int(c) for c in str(num)]
        return ans

# want a better one without str() method... bit operation.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            tmp = digits[i] + carry
            if tmp < 10:
                digits[i] = tmp
                return digits
            else:
                digits[i] = 0
                carry = 1
            if i == 0:
                digits.insert(0, 1)
                return digits
