class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        p1 = 0
        ub = m
        for val in nums2:
            while p1 < ub and nums1[p1] < val:
                p1 += 1
            nums1.insert(p1, val)
            nums1.pop()
            ub += 1
