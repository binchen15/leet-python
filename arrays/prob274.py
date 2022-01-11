class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        
        n = len(citations)
        
        if citations[0] == 0:
            return 0
        
        i = 0
        while i < n:
            if citations[i] == i+1:
                return i+1
            elif citations[i] > i+1:
                if i+1 < n and citations[i+1] >= i+2:
                    i += 1
                else:
                    return i+1
            else:
                return i
