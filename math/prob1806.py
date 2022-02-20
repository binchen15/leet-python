class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        init = [i for i in range(n)]
        
        def operation(perm):
            arr = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[ n // 2 + (i-1) // 2]
                    
            return arr
        
        clone = [i for i in range(n)]
        cnts = 0
        while True:
            clone = operation(clone)
            cnts += 1
            if clone == init:
                break
                
        return cnts
