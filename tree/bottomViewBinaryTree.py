# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1?page=1&category[]=Tree&curated[]=1&sortBy=submissions
class Solution:
    def bottomView(self, root):
        # code here

        vmap = {}
        vmap[0] = [0, 0, 0, root.data] # row, col, index, val

        cur = [ (0, 0, root)]
        nxt = []

        while True:
            while cur:
                row, col, node = cur.pop(0)
                if node.left:
                    nxt.append((row+1, col-1, node.left))
                if node.right:
                    nxt.append((row+1, col+1, node.right))

            if nxt:
                for i, t in enumerate(nxt):
                    v = [t[0], t[1], i, t[2].data]
                    col = v[1]
                    if col not in vmap:
                        vmap[col] = v
                    else:
                       if v[0] > vmap[col][0] or  (v[0] == vmap[col][0] and v[2] > vmap[col][2]):
                           vmap[col] = v
                cur = nxt
                nxt = []
            else:
                break

            # print(vmap)

        p = [ [v[1], v[3]] for v in vmap.values()]

        p.sort(key = lambda x: x[0])
        # print(p)
        return [ v[1] for v in p]
