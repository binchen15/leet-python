# https://practice.geeksforgeeks.org/problems/binary-searchable-elements/1?page=3&category[]=Greedy&sortBy=submissions

class Solution:
    def binarySearchable(self, Arr, n):
        # code here

        dp1 = [0] * n
        dp2 = [0] * n

        dp1[0] = Arr[0]
        dp2[n-1] = Arr[n-1]

        # cumulative maximum left to right
        for i in range(1, n):
            dp1[i] = max(Arr[i], dp1[i-1])

        # cumulative minimum right to left
        for i in range(n-2, -1, -1):
            dp2[i] = min(Arr[i], dp2[i+1])

        cnts = 0
        for i in range(n):
            if (i == 0 and dp2[i+1] > Arr[i]) or \
                (i == n-1 and dp1[i-1] < Arr[i]) or \
                (dp1[i-1] < Arr[i] and dp2[i+1] > Arr[i]):
                cnts += 1

        return cnts
