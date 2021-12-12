class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        n = len(nums)
        
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        def bs(l, r, target):
            if target < nums[l] or target > nums[r]:
                return -1
            while l <= r:
                mid = (l+r)//2
                val = nums[mid]
                if val == target:
                    return mid
                elif val > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        
        
        def findMaxIndex():
            """this assume nums is indeed rotated"""
            l, r = 0, n-1
            while l <= r:
                mid = (l+r)//2
                val = nums[mid]
                if val == nums[l]:
                    return l if nums[l] > nums[r] else r
                elif val > nums[l]:
                    l = mid
                else:
                    r = mid-1
            #return r
        
           
        if nums[0] < nums[n-1]:  # no rotation
            i = bs(0, n-1, target)
            return i
        
        i_max = findMaxIndex()
        # print(f"i_max={i_max}")
        c1 = bs(0, i_max, target)
        c2 = bs(i_max+1, n-1, target)
        if c1 == -1:
            return c2
        else:
            return c1

