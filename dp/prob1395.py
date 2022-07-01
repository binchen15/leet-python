# n^2 solution
class Solution:
    def numTeams(self, rating: List[int]) -> int:

        r = rating
        n = len(r)


        ans = 0
        for i in range(n):
            bl, bg = 0, 0
            al, ag = 0, 0
            v = r[i]
            for j in range(i):
                if r[j] < v:
                    bl += 1
                elif r[j] > v:
                    bg += 1

            for j in range(i+1, n):
                if r[j] < v:
                    al += 1
                elif r[j] > v:
                    ag += 1

            ans += bl * ag + bg * al

        return ans
