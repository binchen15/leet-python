class Solution:
    def mySqrt(self, x: int) -> int:

        if x <= 1:
            return x
 
        l = 1
        while l*l <= x:
            l += 1
 
        return l-1

class Solution:
    def mySqrt(self, x: int) -> int:

        if x <= 1:
            return x

        l, r = 1, x
        while l <= r:
            mid = (l+r)//2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp < x:
                l = mid +1
            else:
                r = mid - 1

        return r

