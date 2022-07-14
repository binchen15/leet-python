# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1/?page=1&category[]=Greedy&sortBy=submissions#

class Solution:

    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):

        # code here
        Jobs.sort(key=lambda job: job.profit, reverse=True)
        slots = set()

        cnts = 0
        profit = 0

        def helper(deadline):
            for i in range(deadline, 0, -1):
                if i not in slots:
                    return i
            return -1



        for job in Jobs:
            i = helper(job.deadline)
            if i != -1:
                slots.add(i)
                profit += job.profit
                cnts += 1

        return [cnts, profit]
