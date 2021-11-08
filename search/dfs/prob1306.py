# 1306 Jump Game III

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        targets = {i for i, _ in enumerate(arr) if arr[i] == 0}
        if not targets:
            return False

        result = False
        def dfs(curr, traversed):

            nonlocal result
            if result:
                return
            if curr in targets:
                result = True
                return
            if curr in traversed:
                return

            traversed.add(curr)
            nxts = filter(lambda x: 0 <= x < n, [curr+arr[curr], curr-arr[curr]])
            for nxt in nxts:
                dfs(nxt, traversed)

        dfs(start, set())

        return result
