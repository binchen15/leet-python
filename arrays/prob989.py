# 989 Aadd to Array-Form of an integer

# 10% slow solution
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        num = self.toNum(A) + K
        return self.toArr(num)

    def toNum(self, A):
        num = 0
        for d in A:
            num = num * 10 + d
        return num

    def toArr(self, n):
        if n == 0:
            return [0]
        arr = []
        while n > 0:
            d = n % 10
            arr.insert(0, d)
            n = n // 10
        return arr

# 70% solution
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        num = int("".join(map(str, A))) + K
        return map(int, str(num))

