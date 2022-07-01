class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def helper(val):
            steps = 0
            while val != 1:
                if val % 2 == 0:
                    val //= 2
                else:
                    val = 3 * val + 1
                steps += 1
            return steps
        
        class Num:
            def __init__(self, val):
                self.val = val
                self.power = helper(val)
                
            def __lt__(self, other):
                if self.power == other.power:
                    return self.val < other.val
                return self.power < other.power
            
        numbers = [ Num(v) for v in range(lo, hi+1)]
        numbers.sort()
        return numbers[k-1].val

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        @lru_cache(maxsize=None)
        def helper(val):
            if val == 1:
                return 0
            if not val & 1:
                val = val >> 1
            else:
                val = 3 * val + 1
            return 1 + helper(val)


        class Num:
            def __init__(self, val):
                self.val = val
                self.power = helper(val)

            def __lt__(self, other):
                if self.power == other.power:
                    return self.val < other.val
                return self.power < other.power

        numbers = [ Num(v) for v in range(lo, hi+1)]
        numbers.sort()
        return numbers[k-1].val

