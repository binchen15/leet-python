class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        
        n1 = len(str1)  # smaller
        n2 = len(str2)
        
        for i in range(n1, 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                tmp = str1[:i]
                #print(tmp)
                if str1.count(tmp) == (n1 / i) and str2.count(tmp) == (n2 / i):
                    return tmp
                
        return ""
