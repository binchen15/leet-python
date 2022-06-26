# create binary tree from descriptions

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        seen = {}
        children  = set()

        for pVal, cVal, left in descriptions:

            if pVal not in seen:
                seen[pVal] = TreeNode(pVal)
            pNode = seen[pVal]

            if cVal not in seen:
                seen[cVal] = TreeNode(cVal)
            cNode = seen[cVal]

            children.add(cVal)

            if left:
                pNode.left = cNode
            else:
                pNode.right =cNode

        # print(seen.keys())
        # print(children)
        rVal = list(set(seen.keys()).difference(children))[0]

        return seen[rVal]
