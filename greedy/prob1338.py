# Reduce Array size to half

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        m = len(arr)

        d = {}
        for n in arr:
            d[n] = d.get(n, 0) + 1

        candies = list(d.items())
        candies.sort(key=lambda x: x[1], reverse=True)

        answer = 0
        size = 0
        for _, cnt in candies:
            size += cnt
            answer += 1
            if size >= m // 2:
                return answer
