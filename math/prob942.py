# 942 DI String Match

# Brutal force. timelimit error. 70/75 cases 
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """      
        n    = len(S)
        nums = list(range(n+1))
        mask = [False] * (n + 1)
        
        tree = {} 
        for i in range(n+1):
            tree[i] = {}
            self.grow(n, i, 0, tree[i], nums, mask[:i]+[True]+mask[i+1:], S)
            
        return self.findPath(n+1, tree)
        
    def grow(self, n, key, k, tree, nums, mask, S):
        if k == n: # all filled
            return
        trend = S[k]
        for i in range(n+1):
            if not mask[i]:
                val = nums[i]
                if (trend == "I" and val > key) or \
                   (trend == "D" and val < key):
                    tree[val] = {}
                    self.grow(n, val, k+1, tree[val], nums, mask[:i]+[True]+mask[i+1:],S)
                    
                    
    def findPath(self, n, tree):
        if n == 1:
            if tree:
                for key in tree:
                    return [key]  # any one is fine
            else:
                return False
        if not tree:
            return False
        for key in tree:
            ans = self.findPath(n-1, tree[key])
            if ans:
                return [key] + ans
        return False
            
# back. still timelimit error. 90/95 case passed
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n    = len(S)
        nums = list(range(n+1))
        mask = [False] * (n+1)  # visited or not
        
        path = []
        for i in range(n+1):
            path.append(i)
            mask[i] = True
            flag = self.backtrack(n, path, nums, mask, S)
            if flag:
                return path
            else:
                path.pop()
                mask[i] = False
            
    def backtrack(self, n, path, nums, mask, S):
        k = len(path)
        if k == n + 1:
            return True
        last = path[-1]
        DI   = S[k-1]
        for i in range(n+1):
            if not mask[i]:
                val = nums[i]
                if (DI == "I" and val > last) or \
                   (DI == "D" and val < last):
                    path.append(val)
                    mask[i] = True
                    flag = self.backtrack(n, path, nums, mask, S)
                    if flag:
                        return True
                    else:
                        path.pop()
                        mask[i] = False
        return False
                    
# use set insted of lists for nums. but still same
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n    = len(S)
        nums = set(range(n+1))
        
        path = []
        for i in range(n+1):
            path.append(i)
            nums.remove(i)
            flag = self.backtrack(n, 1, path, nums, S)
            if flag:
                return path
            else:
                path.pop()
                nums.add(i)
            
    def backtrack(self, n, k, path, nums, S):
        if k == n + 1:
            return True
        last = path[-1]
        DI   = S[k-1]
        for i in range(n+1):
            if i in nums:
                if (DI == "I" and i > last) or \
                   (DI == "D" and i < last):
                    path.append(i)
                    nums.remove(i)
                    flag = self.backtrack(n, k+1, path, nums, S)
                    if flag:
                        return True
                    else:
                        path.pop()
                        nums.add(i)
        return False
                    

# ok. two pointers solution.
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n    = len(S)
        l, h = 0, n
        ans  = []
        for c in S:
            if c == "I":
                ans.append(l)
                l += 1
            else:
                ans.append(h)
                h -= 1
        ans.append(l)
        return ans        

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        n = len(s)
        nums = [i for i in range(0, n+1)]
        
        ans = []
        for c in s:
            if c == "D":
                ans.append(nums.pop())
            else:
                ans.append(nums.pop(0))
                
        ans.append(nums[0])
        
        return ans
                
