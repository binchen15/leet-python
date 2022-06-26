class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.maxDepth = 0
        self.deepest = []
        
        def isLeaf(node):
            return node and not node.left and not node.right
        
        def dfs(path, depth):
            if not path:
                return
            node = path[-1]
            if isLeaf(node):
                if depth < self.maxDepth:
                    return
                elif depth > self.maxDepth:
                    self.maxDepth = depth
                    self.deepest = [path]
                    return
                else:
                    self.deepest.append(path)
                    return 
            else:
                if node.left:
                    dfs(path + [node.left], depth+1)
                if node.right:
                    dfs(path + [node.right], depth+1)
                    
        dfs([root], 0) 
       
        routes = self.deepest
        m = len(routes)
        if m == 1:
            return routes[0][-1]
        
        i = 0
        while i < len(routes[0]):
            node = routes[0][i]
            for j in range(1, m):
                if routes[j][i] != node:
                    # split on index i, so i-1 should be it
                    return routes[0][i-1]
            i += 1
                
        assert False
