class Solution:
    def totalMoney(self, n: int) -> int:
        
        weeks, days = divmod(n, 7)
        
        tot = 0
        
        for w in range(weeks):
            start = w + 1
            end = start + 6
            tmp = 7*(start + end) // 2
            tot += tmp
            
        if days:
            start = weeks+1
            end = start + days - 1
            tmp = days*(start + end) // 2
            tot += tmp
            
        return tot
