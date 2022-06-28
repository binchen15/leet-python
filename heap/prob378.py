class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        hq = []
        
        for i in range(n):
            for j in range(n):
                if len(hq) < k:
                    heapq.heappush(hq, -matrix[i][j])
                else:
                    if matrix[i][j] < -hq[0]:
                        heapq.heappop(hq)
                        heapq.heappush(hq, -matrix[i][j])
        
        return -hq[0]
