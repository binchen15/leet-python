class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        m = len(bank)
        if m == 1:
            return 0
        
        n = len(bank[0])
        
        prev = None

        ans = 0
        
        for i in range(m):
            cur = bank[i]
            cnt = cur.count("1")
            if cnt > 0:
                if not prev:
                    prev = cnt
                else:
                    ans += cnt * prev
                    prev = cnt
                    
        return ans
