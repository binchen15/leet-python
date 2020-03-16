# 501 Find mode in BST

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        wc = {}
        self.inorder(root, wc)
        maxfrq = max(wc.values())
        ans = [ key for key in wc if wc[key] == maxfrq]
        return ans
        
    def inorder(self, root, wc):
        if not root:
            return
        if root.left:
            self.inorder(root.left, wc)
        val = root.val
        wc[val] = wc.get(val, 0) + 1
        if root.right:
            self.inorder(root.right, wc)
            
