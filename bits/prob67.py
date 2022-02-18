class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if a == "0":
            return b
        if b == "0":
            return a
        
        n = max(len(a), len(b))
        
        n1, n2 = len(a), len(b)
        
        a = "0" * (n-n1) + a  # padding to same length
        b = "0" * (n-n2) + b
        
        arr1 = list(map(int, list(a)))
        arr2 = list(map(int, list(b)))
        
        carry = [0] * (n+1)  # carry
        
        ans = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            tmp = arr1[i] + arr2[i] + carry[i+1]
            tmp, r = divmod(tmp, 2)
            ans[i+1] = r
            carry[i] = tmp
            
        ans[0] = carry[0]
        if ans[0] == 0:
            return "".join(map(str, ans[1:]))
        else:
            return "".join(map(str, ans))
