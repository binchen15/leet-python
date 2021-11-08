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


