# 30% solution       
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = []
        self.inorder(root, vals)
        for i in range(len(vals)):
            a = vals[i]
            b = k - a
            if b in vals:
                if b != a:
                    return True
                else:
                    if vals.count(a) >= 2:
                        return True
        return False
            
    def inorder(self, root, vals):
        if not root:
            return
        if root.left:
            self.inorder(root.left, vals)
        vals.append(root.val)
        if root.right:
            self.inorder(root.right, vals)

# not any better
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = []
        self.inorder(root, vals)
        for i in range(len(vals)):
            a = vals[i]
            b = k - a
            if a == b:
                if vals.count(a) >= 2:
                    return True
            else:
                if self.search(vals, b):
                    return True
        return False
        
    def inorder(self, root, vals):
        if not root:
            return
        if root.left:
            self.inorder(root.left, vals)
        vals.append(root.val)
        if root.right:
            self.inorder(root.right, vals)
            
    def search(self, vals, num):
        m = len(vals)
        l, h = 0, m-1
        while l <= h:
            mid = l + (h-l)//2
            if vals[mid] == num:
                return True
            elif vals[mid] < num:
                l = mid + 1
            else:
                h = mid - 1
        return False

# even worse
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = []
        wc   = {}
        self.inorder(root, vals, wc)
        for i in range(len(vals)):
            a = vals[i]
            b = k - a
            if a == b:
                if wc[a] >= 2:
                    return True
            else:
                if self.search(vals, b):
                    return True
        return False
        
    def inorder(self, root, vals, wc):
        if not root:
            return
        if root.left:
            self.inorder(root.left, vals, wc)
        vals.append(root.val)
        wc[root.val] = wc.get(root.val, 0) + 1
        if root.right:
            self.inorder(root.right, vals, wc)
            
    def search(self, vals, num):
        m = len(vals)
        l, h = 0, m-1
        while l <= h:
            mid = l + (h-l)//2
            if vals[mid] == num:
                return True
            elif vals[mid] < num:
                l = mid + 1
            else:
                h = mid - 1
        return False
        

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = []
        self.inorder(root, vals)
        for i in range(len(vals)):
            a = vals[i]
            b = k - a
            curr = self.findValue(root, b)
            if not curr:
                continue
            if curr ==    
                return True
        return False
        
    def inorder(self, root, vals):
        if not root:
            return
        if root.left:
            self.inorder(root.left, vals)
        vals.append(root.val)
        if root.right:
            self.inorder(root.right, vals)
            
    def findValue(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.findValue(root.left, val)
        else:
            return self.findValue(root.right, val)
        
# different solution
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = []
        self.inorder(root, vals)
        for i in range(len(vals)):
            a = vals[i]
            b = k - a
            curr = self.findValue(root, b)
            if curr:
                if a == b: # need find another instance
                    if self.findValue(curr.left, b) or \
                       self.findValue(curr.right, b):
                        return True
                else:
                    return True
        return False
        
    def inorder(self, root, vals):
        if not root:
            return
        if root.left:
            self.inorder(root.left, vals)
        vals.append(root.val)
        if root.right:
            self.inorder(root.right, vals)
            
    def findValue(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.findValue(root.left, val)
        else:
            return self.findValue(root.right, val)
        
 
