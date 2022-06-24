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

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        memo = {}

        def walk(root):
            if not root:
                return
            memo[root.val] = memo.get(root.val, 0) + 1

            walk(root.left)
            walk(root.right)

        walk(root)

        ub = max(memo.values())

        ans = []
        for k, v in memo.items():
            if v == ub:
                ans.append(k)

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        self.max_cnt = 0
        self.cur_val = None
        self.cur_cnt = 0
        
        def walk(node):
            if not node:
                return
            walk(node.left)
            
            # visit current node
            if node.val == self.cur_val:
                self.cur_cnt += 1
            else:
                self.cur_cnt = 1
                self.cur_val = node.val
                
            if self.cur_cnt == self.max_cnt:
                self.res.append(self.cur_val)
            elif self.cur_cnt > self.max_cnt:
                self.max_cnt = self.cur_cnt
                self.res = [self.cur_val]
                
            walk(node.right)
            
        walk(root)
        return self.res
