class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        ans = 0  # number of complete rows
        coins = n
        i = 1
        while coins > 0:
            if coins >= i:
                ans += 1
                coins -= i
                i += 1
            else:
                break
                
        return ans
