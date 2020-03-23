# 1200 Minimum absolute difference

# 40% solution
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort() # nlog(n)
        m = len(arr)
        md = arr[1] - arr[0]
        for i in range(2, m):
            md = min(md, arr[i]-arr[i-1])
        ans = []
        for i in range(m-1):
            if arr[i+1] - arr[i] == md:
                ans.append([arr[i], arr[i+1]])
        return ans


# slightly faster 80%
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort() # nlog(n)
        m = len(arr)
        #md = arr[1] - arr[0]
        #for i in range(2, m):
        #    md = min(md, arr[i]-arr[i-1])
        da = [ arr[i+1] - arr[i] for i in range(m-1) ]
        md = min(da)
        ans = []
        for i in range(m-1):
            if arr[i+1] - arr[i] == md:
                ans.append([arr[i], arr[i+1]])
        return ans
        
        
