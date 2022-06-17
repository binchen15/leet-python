# 10% solution
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        ans = 0
        
        n = len(colors)
        
        for i in range(n-1):
            for j in range(n-1,i,-1):
                if colors[i] != colors[j]:
                    d = abs(j-i)
                    if d > ans:
                        ans = d
                    break
                           
        return ans

# 40%
class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        ans = 0

        n = len(colors)
        seen = set()
        for i in range(n-1):
            if colors[i] in seen:
                continue
            seen.add(colors[i])
            for j in range(n-1,i,-1):
                if colors[i] != colors[j]:
                    d = abs(j-i)
                    if d > ans:
                        ans = d
                    break

        return ans

# 60% solution
class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        ans = 0
        n = len(colors)
        seen = set()

        for i in range(n-1):
            if colors[i] in seen:
                continue
            seen.add(colors[i])
            for j in range(n-1,i,-1):
                if colors[i] != colors[j]:
                    d = j-i
                    if d > ans:
                        ans = d
                    break

        return ans

