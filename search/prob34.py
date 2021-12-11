class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        
        l, r = 0, n - 1
        
        def findAnchor(l, r):
            while l <= r:
                mid = (l + r) // 2
                val = nums[mid]
                if val == target:
                    return mid
                elif val > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        
        anchor = findAnchor(l,r)
        
        if anchor == -1:
            return [-1, -1]
    
        
        def findLeft(l, r):
            if l == r:
                return r
            while l < r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    r = mid
                else:
                    l = mid+1
            return r
        
        def findRight(l, r):
            if l == r:
                return l
            while l < r:
                mid = (l+r+1) // 2
                if nums[mid] == target:
                    l = mid
                else:
                    r = mid-1
            return l
        
        
        return [findLeft(0, anchor), findRight(anchor, n-1)]

