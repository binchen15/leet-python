class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return "0"
        
        flag = num > 0
        
        num = abs(num)
        
        ans = ""
        
        while num > 0:
            num, r = divmod(num, 7)
            ans = str(r) + ans
            
        if not flag:
            ans = "-" + ans
            
        return ans
