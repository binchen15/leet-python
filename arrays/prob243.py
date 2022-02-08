class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        l1 = []
        l2 = []
        
        for i, w in enumerate(wordsDict):
            if w == word1:
                l1.append(i)
            elif w == word2:
                l2.append(i)
                
        ans = sys.maxsize
        
        for i in l1:
            for j in l2:
                if abs(i-j) < ans:
                    ans = abs(i-j)
                    
        return ans
