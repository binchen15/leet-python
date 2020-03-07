class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = len(nums)
        bag = set()  # indices already taken
        i = 0
        rec = 1      # max length of orbits
        while i < m:
            if i in bag:
                i += 1
            else:
                orbit = self.orbit_from_i(nums, i, bag)
                rec = max(rec, len(orbit))
                i += 1
        return rec
        
                            
    def orbit_from_i(self, nums, i, bag):
        # build an orbit from index i
        orbit = set()
        curr  = i
        while nums[curr] not in orbit:
            orbit.add(nums[curr])
            bag.add(curr)  # curr spot taken already
            curr = nums[curr]
        return orbit
    
        
