class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        mini = min(nums)
        maxi = max(nums)
        
        i_mini = nums.index(mini)
        i_maxi = nums.index(maxi)
        
        if mini == maxi:
            return 1
        
        if i_mini < i_maxi:
            l, r = i_mini, i_maxi
        else:
            l, r = i_maxi, i_mini
            
        return min(r+1, n-l, l+1+n-r )
