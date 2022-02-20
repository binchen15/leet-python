# time limit error
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        n = len(arr)
        ans = 0
        
        for i in range(n-1):
            for j in range(i+1, n):
                
                a = arr[i]
                for p in range(i+1, j):
                    a ^= arr[p]
                
                for k in range(j, n):
                    b = arr[j]
                    for q in range(j+1, k+1):
                        b ^= arr[q]
                        
                    if a == b:
                        ans += 1
                        
        return ans

# 20% solution
class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        n = len(arr)
        ans = 0

        for i in range(n-1):
            a = 0
            for j in range(i+1, n):
                a ^= arr[j-1]
                b = 0
                for k in range(j, n):
                    b ^= arr[k]
                    if a == b:
                        ans += 1

        return ans
