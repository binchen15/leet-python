# super ugly number
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        ans = [1]
        counts = {p: 0 for p in primes}

        for i in range(1, n):
            cs = [ ans[v]* p  for p, v in counts.items() ]
            tmp = min(cs)
            ans.append(tmp)
            for p, v in counts.items():
                if tmp == ans[v] * p:
                    counts[p] += 1

        return ans[-1]
