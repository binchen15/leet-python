# 95 unique BST II 

# 5% solution
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """     
        nums = range(1, n+1)
        mask = [1] * n
        if n == 1:
            return [TreeNode(1)]
        
        trees = []
        for i in range(1, n+1):
            root = TreeNode(i)
            mask[i-1] = 0
            self.grow(root, nums, mask, trees)
            mask[i-1] = 1
            
        return trees
     
    def clone(self, head, tree):
        """clone head to tree"""
        if not head:
            return
        if head.left:
            tree.left = TreeNode(head.left.val)
            self.clone(head.left, tree.left)
        if head.right:
            tree.right = TreeNode(head.right.val)
            self.clone(head.right, tree.right)
            
        
    def grow(self, head, nums, mask, trees):
        """assume head not None"""
        if sum(mask) == 0: # no more number:
            for t in trees:
                if self.sameTree(t, head):
                    return
            tree = TreeNode(head.val)
            self.clone(head, tree)
            trees.append(tree)
            return 
        for i, n in enumerate(nums):
            if mask[i]:
                mask[i] = 0
                v = nums[i]
                self.insertNumber(head, v)
                self.grow(head, nums, mask, trees)
                self.removeNumber(head, v)
                mask[i] = 1
        
    def insertNumber(self, head, v):
        """assume head is not None"""
        rv = head.val
        if v < rv:  # left
            if not head.left:
                node = TreeNode(v)
                head.left = node
            else:
                self.insertNumber(head.left, v)
        else:       # right
            if not head.right:
                node = TreeNode(v)
                head.right = node
            else:
                self.insertNumber(head.right, v)
                
      
    def removeNumber(self, head, v):
        """assume v is a leaf node, and it exists..."""
        rv = head.val
        if v < rv:
            if head.left.val == v:
                head.left = None
            else:
                self.removeNumber(head.left, v)
        else:
            if head.right.val == v:
                head.right = None
            else:
                self.removeNumber(head.right, v)
                
    def sameTree(self, head1, head2):
        if  (head1 and not head2) or \
            (head2 and not head1):
            return False
        if not head1 and not head2:
            return True
        return head1.val == head2.val and \
            self.sameTree(head1.left,  head2.left) and \
            self.sameTree(head1.right, head2.right)
    
        
