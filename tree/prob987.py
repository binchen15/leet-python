# https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?page=1&category[]=Tree&curated[]=1&sortBy=submissions

class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        vals = [(0, 0, 0, root.data)]  # vlev, hlev, layer-index,
        cur = [(0, root)]
        nxt = []
        cnt = 1
        while True:
            while cur:
                lev, node = cur.pop(0)
                if node.left:
                    nxt.append((lev-1, node.left))
                if node.right:
                    nxt.append((lev+1, node.right))
            if nxt:
                for i, p in enumerate(nxt):
                    vals.append( (p[0], cnt, i, p[1].data) )
                cur = nxt
                nxt = []
                cnt += 1
            else:
                break
            
        vals.sort(key = lambda x: x[:3])
        
        return [v[3] for v in vals]

