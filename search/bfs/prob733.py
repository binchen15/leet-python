class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        flooded = set()
        
        cur = [(sr, sc)]
        nxt = []
        
        while True:
            while cur:
                r, c = cur.pop(0)
                image[r][c] = newColor
                flooded.add((r,c))
                nbrs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                nbrs = [(r, c) for r, c in nbrs if 0 <= r < m and 0 <= c < n \
                        and image[r][c] == oldColor and (r, c) not in flooded]
                nxt.extend(nbrs)
            if not nxt:
                break
            else:
                cur = nxt
                nxt = []
                
        return image

# not faster
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        flooded = set()
        
        cur = [(sr, sc)]
        nxt = []
        flooded.add((sr, sc))
        while True:
            while cur:
                r, c = cur.pop(0)
                image[r][c] = newColor
                # flooded.add((r,c))
                nbrs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                nbrs = [(r, c) for r, c in nbrs if 0 <= r < m and 0 <= c < n \
                        and image[r][c] == oldColor and (r, c) not in flooded]
                nxt.extend(nbrs)
                for x, y in nbrs:
                    flooded.add((x,y))
            if not nxt:
                break
            else:
                cur = list(set(nxt))
                nxt = []
                
        return image
                
