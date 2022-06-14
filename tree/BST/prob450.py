# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        node = self.findNode(root, key)
        if not node:
            return root
        
        # node is a leaf
        if not node.left and not node.right:
            return self.deleteLeafNode(root, node)
            
        # swap must be either leaf, or one-legged
        swap = self.findSwap(node)
        val = swap.val
        
        # swap itself is leaf
        if not swap.left and not swap.right:
            node = self.deleteLeafNode(node, swap)
            #if node:
            #    node.val = val
            node.val = val
        else:
            self.deleteSwap(node, swap)
            node.val = val
        
        return root
        
        
    def findSwap(self, node):
        "biggest on the left subtree, or smallest on right subtree"
        if node.left:
            cur = node.left
            while cur.right:
                cur = cur.right
        else:
            cur = node.right
            while cur.left:
                cur = cur.left
        return cur
        
        
    def findNode(self, root, key):
        "find node with given key"
        if not root:
            return None
        elif root.val == key:
            ans = root
        elif root.val > key:
            ans = self.findNode(root.left, key)
        else:
            ans = self.findNode(root.right, key)
        return ans
        
        
    def deleteLeafNode(self, root, node):
        "assume node is leaf, delete it"
        if root == node:
            return None
        if root.val > node.val:
            root.left = self.deleteLeafNode(root.left, node)
        else:
            root.right = self.deleteLeafNode(root.right, node)
        return root
    
    
    def deleteSwap(self, root, node):
        if root.left == node:
            if node.left:
                root.left = node.left
            else:
                root.left = node.right
        elif root.right == node:
            if node.left:
                root.right = node.left
            else:
                root.right = node.right
        elif root.val > node.val:
            self.deleteSwap(root.left, node)
        else:
            self.deleteSwap(root.right, node)

#  better solution

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:  # find the node to delete
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # root has left & right child
            successor = root.right
            while successor.left is not None:
                successor = successor.left

            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
            return root

