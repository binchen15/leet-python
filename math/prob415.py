class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        n1 = len(num1)  # longer
        n2 = len(num2)
        
        arr1 = list(map(int, list(num1)))
        arr2 = [0] * (n1-n2) + list(map(int, list(num2)))
        carry = [0] * (n1 + 1)
        ans = [0] * (n1 + 1)
        
        for i in range(n1-1, -1, -1):
            tmp = arr1[i] + arr2[i] + carry[i+1]
            tmp, r = divmod(tmp, 10)
            carry[i] = tmp
            ans[i+1] = r
            
        ans[0] = carry[0]
        
        print(arr1, arr2, carry)
        
        if ans[0] == 0:
            return "".join(map(str, ans[1:]))
        else:
            return "".join(map(str, ans))
