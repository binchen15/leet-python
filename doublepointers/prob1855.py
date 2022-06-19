# wrong answer

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        m, n = len(nums1), len(nums2)

        i, j = m-1, 0

        if nums2[0] < nums1[m-1]:
            return 0

        lb, ub = nums1[m-1], nums2[0]

        while lb <= ub:

            while j+1 < n and nums2[j+1] >= lb:
                j += 1

            ub = nums2[j]

            while i-1 >= 0 and nums1[i-1] <= ub:
                i -= 1

            lb = nums1[i]

            if i <= j:
                return j - i
            else:
                return 0

#

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        res = 0

        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                res = max(res, j-i)
                j += 1
            else:
                i += 1

        return res
