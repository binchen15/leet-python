class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        arr = sorted(score, reverse=True)
        
        special = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal"
        }
        
        ranks = {}
        for i, v in enumerate(arr):
            ranks[v] = str(i+1) if i+1 not in special else special[i+1]
                    
        ans = [ranks[v] for v in score]
        return ans
