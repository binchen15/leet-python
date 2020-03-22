#905 Sort array by parity

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in A:
            if n & 1:
                ans.append(n)
            else:
                ans.insert(0, n)
        return ans
           
# inplace, but slow. 5% in speed
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ub = len(A)
        i = 0
        while i < ub:
            a = A[i]
            if a & 1:
                A.remove(a)
                A.append(a)
                ub -= 1
            else:
                i += 1
        return A 

# 93% solution
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        m = len(A)
        l, h = 0, m - 1
        while l < h:
            while l < m and not (A[l] & 1):
                l += 1    
            while h >= 0 and (A[h] & 1):
                h -= 1
            if l >= h:  # l < h guarantees l < m and h > 0 too 
                break
            t    = A[l]
            A[l] = A[h]
            A[h] = t
            l += 1
            h -= 1
        return A
