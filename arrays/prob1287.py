# 1287 Element Appearing more than 25% in sorted array

# 30% solution. did not use the fact that array is sorted
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = len(arr)
        dc = {}
        for n in arr:
            dc[n] = dc.get(n, 0) + 1
        pairs = sorted(dc.items(), key=lambda x : x[1])
        return pairs[-1][0]
        
# better in speed. stop early.
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = len(arr)
        if m < 4:
            return arr[0]
        
        bar = int(math.ceil(m / 4.0))
        
        val = arr[0]
        cnt = 1
        i   = 0
        while i < m:
            while i+1 < m and arr[i+1] == arr[i]:
                cnt += 1
                i   += 1
            if i+1 == m:
                return val
            if cnt > bar:
                return val
            val = arr[i+1] # start with new number
            cnt = 1
            i   += 1
        return None # should not happen
                
                
