# 538 BST to Greater Tree
# 25% solution... slow

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        # return keys as sorted list
        vals = []
        self.inorder(root, vals)
        wc   = {}  # word/value counts
        for v in vals:
            wc[v] = wc.get(v, 0) + 1
            
        keys = sorted(wc.keys(), reverse=True)
        
        sums = {keys[0]:0}  # max key
        for i in range(1, len(keys)):
            key  = keys[i]
            prev = keys[i-1]
            sums[key] = sums[prev] + prev * wc[prev]  
        
        self.greatAgain(root, sums)
        return root
    
            
    def inorder(self, root, vals):
        if not root:
            return
        if root.left:
            self.inorder(root.left, vals)
        vals.append(root.val)
        if root.right:
            self.inorder(root.right, vals)
            
    def greatAgain(self, root, sums):
        if not root:
            return
        root.val += sums.get(root.val, 0)
        self.greatAgain(root.left, sums)
        self.greatAgain(root.right, sums)
        

# 75% solution. recursion. traverse right subtree first
class Solution(object):
    
    total = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.traverse(root)
        return root
        
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.right)
        root.val  += self.total
        self.total = root.val
        self.traverse(root.left)
                
