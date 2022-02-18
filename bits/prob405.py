class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0:
            return "0"
        elif num < 0:
            num = 2 ** 32 - abs(num)
            
        arr = [i for i in range(10)] + list("abcdef")
        
        ans = ""
        while num > 0:
            num, r = divmod(num, 16)
            ans = str(arr[r]) + ans
            
        return ans
