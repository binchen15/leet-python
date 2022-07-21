# stock span
# https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1?page=1&company[]=Amazon&curated[]=1&sortBy=submissions
class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        
        ans = [1]
        stack = [[a[0], 1]]
        
        for i in range(1, n):
            tmp = 1
            if a[i] < stack[-1][0]:
                ans.append(1)
                stack.append([a[i], 1])
            else:
                while stack and a[i] >= stack[-1][0]:
                    tmp += stack[-1][1]
                    stack.pop()
                ans.append(tmp)
                stack.append([a[i], tmp])
                
        return ans
