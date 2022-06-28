class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = {}  # all the edges between vertices
        graph[target.val] = set()
        
        def walk(root):
            if not root:
                return
            v = root.val
            if root.left:
                l = root.left.val
                if v in graph:
                    graph[v].add(l)
                else:
                    graph[v] = set([l])
                    
                if l in graph:
                    graph[l].add(v)
                else:
                    graph[l] = set([v])
                    
                walk(root.left)
                
            if root.right:
                r = root.right.val
                if v in graph:
                    graph[v].add(r)
                else:
                    graph[v] = set([r])
                    
                if r in graph:
                    graph[r].add(v)
                else:
                    graph[r] = set([v])
                    
                walk(root.right)
                
        walk(root)
        
        #print(graph)
        
        seen = set()
        distance = 0
        cur = [target.val]
        nxt = []
        seen.add(target.val)
        
        
        while distance < k:
            while cur:
                node = cur.pop(0)
                for v in graph[node]:
                    if v in seen:
                        continue
                    else:
                        seen.add(v)
                        nxt.append(v)
            
            distance += 1
            cur = nxt
            nxt = []
            
        return cur
