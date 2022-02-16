class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        flags = []
        
        subsets = set()
        
        def walk(flags, i):
            if i == n:
                indices = []
                for i in range(n):
                    if flags[i]:
                        indices.append(i)
                subsets.add(tuple(indices))
                return 
            
            flags.append(False)
            walk(flags, i+1)
            flags.pop()
            flags.append(True)
            walk(flags, i+1)
            flags.pop()
            
        walk(flags, 0)
        
        ans = 0
        
        for t in subsets:
            tmp = 0
            for i in t:
                tmp ^= nums[i]
            ans += tmp
            
        return ans

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        flags = []
        subsets = set()
        
        def walk(flags, i):
            if i == n:        
                subsets.add(tuple(flags))
                return 
            
            walk(flags, i+1)
            flags.append(i)
            walk(flags, i+1)
            flags.pop()
            
        walk(flags, 0)
        
        ans = 0
        
        for t in subsets:
            tmp = 0
            for i in t:
                tmp ^= nums[i]
            ans += tmp
            
        return ans

