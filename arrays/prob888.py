# 888 Fair Candy Swap

# time limit error
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sizeA = sum(A)
        sizeB = sum(B)
        diff = (sizeA - sizeB) // 2 # should be even.
        
        for n in A:
            for m in B:
                if n - m == diff:
                    return [n, m]

# double pointer, 40% solution
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sizeA = sum(A)
        sizeB = sum(B)
        diff = (sizeA - sizeB) // 2 # should be even.
        
        A.sort() # n*log(n)
        B.sort()
        
        i = 0 # len(A) - 1
        j = 0
        while A[i] - B[j] != diff:
            if A[i] - B[j] < diff:
                i += 1
            else:
                j += 1
        return [A[i], B[j]]
    
# hashmap. 80% solution
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sizeA = sum(A)
        sizeB = sum(B)
        diff = (sizeA - sizeB) // 2 # should be even.
        # look for a in A, b in B such that a - b = diff
        # a = b + diff
        hmap = { diff+b : b for b in B}
        for a in A:
            if a in hmap:
                return [a, hmap[a]]
        

