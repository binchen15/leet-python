class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        ans = [0] * num_people
        cnt = 1
        pos = 0
        
        while candies > 0:
            if candies <= cnt:
                ans[pos] += candies
                break
            else:
                ans[pos] += cnt
                candies -= cnt
                cnt += 1
                pos += 1                
                pos %= num_people
                
        return ans
