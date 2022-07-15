#barely pass all cases.
# https://practice.geeksforgeeks.org/problems/e47329920b4e75869ea7b0e9b7c59ea145ccc22c/1/?page=2&category[]=Greedy&sortBy=submissions#
class Solution:
    def catchThieves(self, arr, n, k):
        # code here
        # cnts = 0
        caught = set()

        ub = arr.count("T")
        if ub == 0 or ub == len(arr):
            return 0

        lb = 0
        for i in range(n):
            if arr[i] == "P":  # a policeman
                flag = False # did police i catch a thief
                for j in range(i-k, i+k+1):
                    if lb <= j < n and arr[j] == "T" and j not in caught:
                        # cnts += 1
                        caught.add(j)
                        lb = j+1
                        flag = True
                        if len(caught) == ub:
                            return len(caught)
                        break
                if not flag:
                    lb = i+k

        return len(caught)
