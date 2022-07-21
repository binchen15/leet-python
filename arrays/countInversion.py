# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?page=1&company[]=Amazon&curated[]=1&sortBy=submissions

class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code 
        temp = [0] * n
        cnts = self.mergesort(arr, temp, 0, n-1)
        return cnts
        
    def mergesort(self, arr, temp, left, right):
        cnts = 0
        if left < right:
            mid = (left + right) // 2
            cL = self.mergesort(arr, temp, left, mid)
            cR = self.mergesort(arr, temp, mid+1, right)
            cLR = self.merge(arr, temp, left, mid, right)
            cnts += cL + cR + cLR
        return cnts
        
    def merge(self, arr, temp, left, mid, right):
        i = left
        j = mid+1
        k = left
        cnts = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                k += 1
                i += 1
            else:
                temp[k] = arr[j]
                cnts += mid-i+1
                k += 1
                j += 1
                
        while i <= mid:
            temp[k] = arr[i]
            k += 1
            i += 1
        while j <= right:
            temp[k] = arr[j]
            k += 1
            j += 1
        
        for i in range(left, right+1):
            arr[i] = temp[i]
            
        return cnts
