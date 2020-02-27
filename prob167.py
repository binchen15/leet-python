class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #i = 0
        j = 1
        m = len(numbers)
        while j < m:
            i = 0
            while i < j:
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                elif numbers[i] + numbers[j] > target:
                    break
                else:
                    i += 1
            j += 1
            while j+1 < m and numbers[j] == numbers[j+1]:
                j +=1
                
            
        
