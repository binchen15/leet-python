# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1/?page=1&category[]=Greedy&sortBy=submissions
#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        
        if n == 1:
            return 0
    
        arr.sort()
        
        if arr[n-1] - arr[0] <= k:
            return arr[n-1] - arr[0]
            
        if arr[n-1] < k:
            return arr[n-1] - arr[0]
            
        base = arr[n-1] - arr[0]
        
        i = 0
        if arr[0] < k:
            while i+1 < n and arr[i+1] < k:
                i += 1
            
        for j in range(i, n-1):
            ub = max(arr[n-1]-k, arr[j]+k)
            lb = min(arr[0]+k, arr[j+1]-k)
            base = min(base, ub-lb)
            
        return base
