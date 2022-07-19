# 652 find duplicate trees

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        ans = []
        seen = {}

        def walk(node):
            if not node:
                return ""
            rep = str(node.val) + "[" + walk(node.left) + "," + walk(node.right) + "]"
            if rep not in seen:
                seen[rep] = 1
            else:
                seen[rep] += 1
                if seen[rep] == 2:
                    ans.append(node)

            return rep

        walk(root)

        return ans
