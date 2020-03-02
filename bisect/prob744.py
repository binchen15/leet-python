class Solution(object):
    """slow"""
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        
        l, h = 0, len(letters)-1
        while l < h:
            mid = l + (h - l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                h = mid
        return letters[l]
        

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for c in letters:
            if c > target:
                return c
        return letters[0] 
