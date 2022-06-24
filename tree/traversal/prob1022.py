class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    
        bag = []
        def walk(tot, node, bag):
            if not node:
                # bag.add(tot)
                return
            else:
                tot = tot * 2 + node.val
                if not node.left and not node.right:
                    bag.append(tot)
                    return
                if node.left:
                    walk(tot, node.left, bag)
                if node.right:
                    walk(tot, node.right, bag)
                    
        walk(0, root, bag)
        # print(bag)
        return sum(bag)

# simplified
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        bag = []
        def walk(tot, node, bag):
            tot = tot * 2 + node.val
            if not node.left and not node.right:
                bag.append(tot)
                return
            if node.left:
                walk(tot, node.left, bag)
            if node.right:
                walk(tot, node.right, bag)

        walk(0, root, bag)
        # print(bag)
        return sum(bag)
