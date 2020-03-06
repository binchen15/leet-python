class Solution(object):
    """failed attempt. Memory error"""
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq = set(nums)
        if not uniq:
            return 0
        
        lb   = min(uniq)
        ub   = max(uniq)
        
        data = [0] * (ub - lb + 1)
        for v in uniq:
            data[v-lb] = 1
            
        ans = 0
        i   = 0
        m   = len(data)
        while i < m:
            while i < m and not data[i]:
                i += 1
            if i == m:
                break
            else:  # data[i] == 1
                cnt = 0
                j   = i
                while j < m and data[j]:
                    cnt += 1
                    j   += 1
                if cnt > ans:
                    ans = cnt
                if j == m:
                    break
                i = j + 1
            
        return ans        
                    
                    
class Solution(object):
    """hash, and recursion to build the path"""
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for n in nums:
            data[n] = 1   # ignore duplicates
            
        for key in data:
            self.forward(data, key)
            
        if not data:
            return 0
        else:
            return max(data.values())
    
    def forward(self, data, n):
        """length of the consecutive sequence starting from n """
        if n not in data:
            return 0
        cnt = data[n]
        if cnt > 1: # already done, simply return in
            return cnt
        else:  # cnt == 1
            if n+1 in data:
                cnt = self.forward(data, n+1) + 1
                data[n] = cnt
            return cnt
            

