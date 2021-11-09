# Prob 269. Graph, Topoligical sort

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        child = collections.defaultdict(set)
        parent = collections.defaultdict(set)

        chars = {c for word in words for c in word}
        for c in chars:
            child[c] = set()
            parent[c] = set()

        valid = True
        def compare(w1, w2, child, parent):
            nonlocal valid
            if w1 == w2:
                return
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                valid = False
                return
            n = min(len(w1), len(w2))
            for i in range(n):
                if w1[i] != w2[i]:
                    child[w1[i]].add(w2[i])
                    parent[w2[i]].add(w1[i])
                    break

        for i in range(len(words)-1):
            if not valid:
                break
            compare(words[i], words[i+1], child, parent)

        if not valid:
            return ""

        # print(g)
        res = []
        q = [char for char in chars if not parent[char]]  # store parentless nodes
        while q:
            node = q.pop(0)
            res.append(node)
            del parent[node]
            for c in child[node]:
                parent[c].remove(node)
                if not parent[c]:
                    q.append(c)

        if parent:
            return ""
        return "".join(res)

