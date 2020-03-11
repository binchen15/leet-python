class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        m = len(nums)
        # bisecting the min and max possible distance
        l, h = 0, nums[-1] - nums[0]
        while l < h:
            mid = l + (h-l)//2
            # how many distances are <= mid 
            cnt = 0
            
            i = 0 # start index
            for j in range(m): # end index 
                while nums[j] - nums[i] > mid:
                    i += 1
                cnt += j - i
                    
            # continue since it is sorted
            if cnt < k:
                l = mid + 1
            else:        # even if cnt == k, mid might not be the answer
                h = mid  # mid might not even be a valid distance
        return l
