# 5% solution
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        queue = [original]
        queue_clone = [cloned]

        while queue:
            node = queue.pop(0)
            node_clone = queue_clone.pop(0)
            if node.val == target.val:
                return node_clone

            if node.left:
                queue.append(node.left)
                queue_clone.append(node_clone.left)
            if node.right:
                queue.append(node.right)
                queue_clone.append(node_clone.right)

# 95% solution

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def helper(org, clo, tar):
            if not org:
                return None

            if org.val == tar.val:
                return clo

            if org.left:
                tmp = helper(org.left, clo.left, tar)
                if tmp:
                    return tmp

            if org.right:
                return helper(org.right, clo.right, tar)

        return helper(original, cloned, target)
