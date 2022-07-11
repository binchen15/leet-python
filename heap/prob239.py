class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        pq = []
        n = len(nums)
        
        for i in range(k):
            heapq.heappush(pq, -nums[i])
            
        ans = [-pq[0]]
        l = 0
        debts = {}
        for i in range(k, n):
            heapq.heappush(pq, -nums[i])
            togo = -nums[l]
            l += 1
            debts[togo] = debts.get(togo, 0) + 1
            while pq[0] in debts and debts[pq[0]] > 0:
                debts[pq[0]] -= 1
                heapq.heappop(pq)
            ans.append(-pq[0])
            
        return ans
