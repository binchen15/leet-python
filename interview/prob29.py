# 29 divide two integers

# time limit error
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor < 0) or \
            (dividend < 0 and divisor > 0):
            neg = True
        else:
            neg = False
        dividend = dividend if dividend > 0 else -dividend
        divisor  = divisor  if divisor  > 0 else -divisor
        #print(dividend, divisor)
        cnt = 0
        while dividend >= divisor:
            dividend -= divisor
            cnt += 1
        if neg:
            return -cnt
        else:
            return cnt
        
# used math.log, math.pow
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor < 0) or \
            (dividend < 0 and divisor > 0):
            neg = True
        else:
            neg = False
        dividend = dividend if dividend > 0 else 0 - dividend
        divisor  = divisor  if divisor  > 0 else 0 - divisor
        
        ans = int(math.pow(2, math.log(dividend, 2) - math.log(divisor, 2)))
        
        if neg:
            return -ans
        else:
            if ans == 2**31:
                ans -= 1  # maximum integer
                #print(ans)
            return ans

# used >>, << operator
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor < 0) or \
            (dividend < 0 and divisor > 0):
            neg = True
        else:
            neg = False
        dividend = dividend if dividend > 0 else -dividend
        divisor  = divisor  if divisor  > 0 else -divisor
        
        ans  = 0
        cnt  = 1
        while dividend >= divisor:
            while (divisor << 1) <= dividend:
                divisor = divisor << 1
                cnt     = cnt << 1
            dividend -= divisor
            ans      += cnt
            if dividend == 0:
                break
            if cnt == 1 and dividend < divisor:
                break
            while dividend < divisor:
                divisor = divisor >> 1
                cnt = cnt >> 1
                   
        if neg:
            return -ans
        else:
            if ans == 2**31:
                ans -= 1
            return ans
                
