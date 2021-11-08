# 1192 Critical connections in a network

# timelimt error when submit
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        g = collections.defaultdict(set)

        for s, e in connections:
            g[s].add(e)
            g[e].add(s)

        # print(g)

        def reachable(g, start, end):

            flag = False
            def dfs(g, curr, visited):
                nonlocal flag
                if flag:
                    return
                if curr == end:
                    flag = True
                    return
                if curr in visited:
                    return

                visited.add(curr)
                for nxt in g[curr]:
                    dfs(g, nxt, visited)

            dfs(g, start, set())
            return flag

        crit = []
        for conn in connections:
            s, e = conn
            g[s].remove(e)
            g[e].remove(s)
            if not reachable(g, s, e):
                crit.append(conn)
            g[s].add(e)
            g[e].add(s)
        return crit

# this one works. by detecting cycles. O(n) time complexity
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        g = collections.defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)

        res = [] # list of critical edges
        jumps = [-1] * n  # jumps[v] stores the minium level the node v has seen among his children (recursively)
        def DFS(cur, par, lev):  # return the minium level the node cur has seen, excluding self

            jumps[cur] = lev + 1  # expected value if there were no cycles

            for child in g[cur]:
                if child == par:
                    continue
                if jumps[child] == -1:  # not traversed yet
                    jumps[child] = DFS(child, cur, lev + 1)
                jumps[cur] = min(jumps[cur], jumps[child])

            if jumps[cur] == lev + 1 and cur != 0:  # no cycle
                res.append([par, cur])
            return jumps[cur]

        DFS(0, -1, 0)
        return res
