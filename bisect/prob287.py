class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        sz = len(nums)
        n = sz-1
        
        l, r = 1, n
        while l < r:
            mid = (l+r) // 2
            cnt = 0
            cnt = sum([num <= mid for num in nums])
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        return l
