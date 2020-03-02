# this takes like 3 hours.. GOD
class Solution(object):

    """non-decreasing array"""
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = len(nums)
        if m <= 1:
            return True
        token = True  # can use only once   
        for i in range(1, m):
            if nums[i] >= nums[i-1]:
                continue
            else:  # going down
                if not token:
                    return False
                token = False
                # how to use the token is headache
                if i == m - 1:
                    return True
                else: # there is next element
                    if nums[i] > nums[i+1]:
                        return False
                    elif nums[i-1] <= nums[i+1]:
                        if i-2 < 0 or nums[i] >= nums[i-2]:
                            nums[i-1] = nums[i]
                        else:
                            nums[i]   = nums[i-1]
                    else:
                        nums[i-1] = nums[i]
                        if i-2 >= 0 and nums[i-1] < nums[i-2]:
                            return False                
        return True
                   
