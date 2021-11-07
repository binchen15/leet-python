# 133 clone graph
# DFS algorithm

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        cnodes = {}  # cloned nodes key by val of the node

        set1 = set()  # to store vals/nodes already traversed for dfs
        set2 = set()  # to store vals/nodes already traversed for dfs2

        def dfs(node):
            key = node.val
            set1.add(key)
            if key not in cnodes:
                tmp = Node(node.val)
                cnodes[key] = tmp
            if node.neighbors:
                for nbr in node.neighbors:
                    if nbr.val not in set1:
                        dfs(nbr)

        def dfs2(node):
            key = node.val
            set2.add(key)
            cnode = cnodes[key]
            if node.neighbors:
                cnode.neighbors = [cnodes[nbr.val] for nbr in node.neighbors]
                for nbr in node.neighbors:
                    if nbr.val not in set2:
                        dfs2(nbr)

        dfs(node)
        dfs2(node)
        return cnodes[node.val]

# new solution with 1 pass
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        visited = {}

        # visited[node] = Node(node.val)

        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited[node].neighbors.append(dfs(neighbor))
                else:
                    visited[node].neighbors.append(visited[neighbor])

            return visited[node]

        return dfs(node)

