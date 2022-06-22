class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        r = rowIndex
        if r == 0:
            return [1]
        if r == 1:
            return [1, 1]
        
        prev = [1, 1]
        for i in range(r-1):
            size = len(prev)
            nxt = [1] + [0] * (size-1) + [1]
            for j in range(1, size):
                nxt[j] = prev[j-1] + prev[j]
            prev = nxt
    
        return prev
