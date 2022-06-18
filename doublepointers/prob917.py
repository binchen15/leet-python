# 917 reverse only letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        arr = list(s)
        n = len(arr)

        l, r = 0, n-1

        while l < r:
            while not arr[l].isalpha() and l+1 < n:
                l += 1
            while not arr[r].isalpha() and r-1 >= 0:
                r -= 1

            if l < r:
                arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return "".join(arr)
