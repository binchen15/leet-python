class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        tot = sum(arr)
        if tot % 3 != 0:
            return False
        psum = tot // 3
        
        n = len(arr)
        
        i = 0
        tmp = arr[0]
        while tmp != psum and i+1 < n:
            i += 1
            tmp += arr[i]
            
        if tmp != psum:
            return False
        
        j = n-1
        tmp2 = arr[n-1]
        while tmp2 != psum and j-1 >= 0:
            j -= 1
            tmp2 += arr[j]
            
        if tmp2 != psum:
            return False
        
        if i >= j-1:
            return False
        
        return True
