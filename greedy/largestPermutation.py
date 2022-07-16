https://practice.geeksforgeeks.org/problems/largest-permutation1351/1?page=3&category[]=Greedy&sortBy=submissions

class Solution:
    def KswapPermutation(self,arr,n,k):

        #arr2 = sorted(arr, reverse=True) # key=str,

        hmap = {v:i for i, v in enumerate(arr)}

        i = 0
        cnts = 0  # number of swaps
        while i < n:
            v = n-i
            if arr[i] != v:
                j = hmap[v] # arr.index(arr2[i])
                hmap[v] = i
                hmap[arr[i]] = j
                arr[i], arr[j] = arr[j], arr[i]
                cnts += 1
                if cnts == k:
                    break
            i += 1
