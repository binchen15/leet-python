class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        memo = {}
        
        def helper(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            else:
                memo[root] = root.val + helper(root.left) + helper(root.right)
                return memo[root]
            
        helper(root)
        
        cnts = {}
        
        for val in memo.values():
            cnts[val] = cnts.get(val, 0) + 1
            
        max_freq = max(cnts.values())
        
        ans = [ key for key in cnts if cnts[key] == max_freq]
        return ans
