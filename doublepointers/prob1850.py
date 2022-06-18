class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
       
        # find the Kth largest number
        target = num
        for i in range(k):
            target = self.findNext(target)
            
        num = list(num)
        n = len(num)
        cnts = 0 # count number of adjacent swaps needed
        
        for i in range(n):
            if num[i] != target[i]:
                j = i
                while num[j] != target[i]:
                    j += 1
                for m in range(j, i, -1):
                    num[m], num[m-1] = num[m-1], num[m]
                    cnts += 1
                    
        return cnts

