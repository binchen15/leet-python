# https://practice.geeksforgeeks.org/problems/maximum-path-sum/1?page=1&category[]=Tree&curated[]=1&sortBy=submissions
# failed. but suspect the answer is wrong

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def maxPathSum(self, root):
        # code here

        if not root or (not root.left and not root.right):
            return 0

        self.ans = -sys.maxsize

        def walk(node):
            if not node:
               return 0
            ans = node.data
            if node.left:
                l = walk(node.left)
            if node.right:
                r = walk(node.right)

            if node.left and node.right:
                self.ans = max(self.ans, node.data + l + r)

            if node.left and node.right:
                ans += max(l, r)
            elif node.left:
                ans += l
            elif node.right:
                ans += r

            return ans

        walk(root)
        return self.ans
