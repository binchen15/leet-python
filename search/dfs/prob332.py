# reconstruct itenary
# DFS, and backtrack

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        g = collections.defaultdict(dict)
        n = len(tickets)

        for start, end in tickets:
            g[start][end] = g[start].get(end, 0) + 1

        path = ["JFK"]
        result = None
        def dfs(path):
            nonlocal result
            if result:
                return
            if len(path) == n + 1:
                result = path[:]
                return
            cur = path[-1]
            for nxt in sorted(g[cur].keys()):
                if g[cur][nxt] == 0:
                    continue
                g[cur][nxt] -= 1
                path.append(nxt)
                dfs(path)
                path.pop()
                g[cur][nxt] += 1

        dfs(path)

        return result
