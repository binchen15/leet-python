class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def isPalin(bag):
            vals = bag.values()
            cnts = 0 # number of odd values
            for val in vals:
                if val % 2 == 1:
                    cnts += 1        
            return cnts <= 1
        
        def walk(root, bag):
            # print(bag)
            if not root:
                return
            
            bag = dict(bag)
            bag[root.val] = bag.get(root.val, 0) + 1
            
            if not root.left and not root.right:
                if isPalin(bag):
                    self.ans += 1
                return
            if root.left:
                walk(root.left, bag)
            if root.right:
                walk(root.right, bag)
                
        walk(root, {})
        
        return self.ans
