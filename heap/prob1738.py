# time limit error
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        scores = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            tmp = 0
            for j in range(1, n+1):
                tmp ^= matrix[i-1][j-1]
                scores[i][j] = scores[i-1][j] ^ tmp
        
        class Item:
            def __init__(self, i, j):
                self.coord = (i, j)
                self.score = scores[i+1][j+1]
                
            def __lt__(self, other):
                return self.score < other.score
            
        
        pq = []
        
        for i in range(m):
            for j in range(n):
                item = Item(i, j)
                if len(pq) < k:
                    heapq.heappush(pq, item) 
                else:
                    if item > pq[0]:
                        heapq.heappop(pq)
                        heapq.heappush(pq, item)
                        
        return pq[0].score

# time limit again
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:

        m = len(matrix)
        n = len(matrix[0])

        scores = [[0] * (n+1) for _ in range(m+1)]

        class Item:
            def __init__(self, i, j):
                self.coord = (i, j)
                self.score = scores[i+1][j+1]

            def __lt__(self, other):
                return self.score < other.score

        pq = []

        for i in range(1, m+1):
            tmp = 0
            for j in range(1, n+1):
                tmp ^= matrix[i-1][j-1]
                scores[i][j] = scores[i-1][j] ^ tmp

                item = Item(i-1, j-1)
                if len(pq) < k:
                    heapq.heappush(pq, item)
                else:
                    if item > pq[0]:
                        heapq.heappop(pq)
                        heapq.heappush(pq, item)

        return pq[0].score

# 10% solution
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:

        m = len(matrix)
        n = len(matrix[0])

        scores = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            tmp = 0
            for j in range(1, n+1):
                tmp ^= matrix[i-1][j-1]
                scores[i][j] = scores[i-1][j] ^ tmp

        pq = []

        for i in range(1, m+1):
            pq += scores[i][1:]

        return heapq.nlargest(k, pq)[-1]
