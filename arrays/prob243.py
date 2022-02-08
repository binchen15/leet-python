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
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
                
        ans = sys.maxsize
        stack = []
        
        for i, w in enumerate(wordsDict):
            if w in (word1, word2):
                if not stack:
                    stack = (i, w)
                elif stack[1] == w:
                    stack = (i, w)
                else:
                    ans = min(ans, i - stack[0])
                    stack = (i, w)
                
                
        return ans
