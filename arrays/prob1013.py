# 1013 Partition Array into 3 parts with equal sum

# 100% solution. Yeah.
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        m   = len(A)
        tot = sum(A)
        if tot % 3 != 0:
            return False
        psum = tot // 3
        
        i  = 0
        s1 = A[0]
        while s1 != psum and i+1 < m:
            i += 1
            s1 += A[i]
        if i+1 == m:
            return False
        
        j  = m-1
        s3 = A[j]
        while s3 != psum and j-1 >= 0:
            j -= 1
            s3 += A[j]
        if j-1 == 0:
            return False
        if i + 1 >= j:
            return False
        else:
            return True
        
