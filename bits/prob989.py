class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        num1 = num
        num2 = list(map(int, str(k)))
        
        n1, n2 = len(num1), len(num2)
        n = max(n1, n2)
        
        num1 = [0] * (n-n1) + num1
        num2 = [0] * (n-n2) + num2
        carry = [0] * (n+1)
        ans = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            tmp = num1[i] + num2[i] + carry[i+1]
            tmp, r = divmod(tmp, 10)
            ans[i+1] = r
            carry[i] = tmp
            
        ans[0] = carry[0]
        
        if ans[0] == 0:
            ans.pop(0)
            
        return ans
