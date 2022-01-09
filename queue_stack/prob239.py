class MQ:
    "Monotonic Queue"
    
    def __init__(self):
        self.q = []
        
    def popBack(self):
        self.q.pop()
        
    def popFront(self):
        self.q.pop(0)
        
    def push(self, e):
        while self.q and self.q[-1] < e:
            self.popBack()
        self.q.append(e)
        
    def max(self):
        return self.q[0]
            
        
class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        elif k == n:
            return [max(nums)]
        
        mq = MQ()
        ans = []
        for i in range(n):
            mq.push(nums[i])
            if i >= k-1:
                ans.append(mq.max())
                if nums[i-k+1] == mq.max():
                    mq.popFront()
            
        return ans
