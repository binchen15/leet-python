# count how many consecutive ones of the previous number
# 50% solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0] * (n+1)
        
        def helper(i):
            ans = 0
            while i % 2 == 1:
                ans += 1
                i = i >> 1
            return ans
        
        for i in range(1, n+1):
            ans[i] = ans[i-1] + 1 - helper(i-1)
            
        return ans
