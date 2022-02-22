class Solution:
    def minimumSum(self, num: int) -> int:
        
        digits = list(map(int, str(num)))
        digits.sort()
        
        return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]
