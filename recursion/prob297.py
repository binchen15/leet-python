# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = str(root.val)
        if root.left or root.right:
            if root.left and root.right:
                children = f"[{self.serialize(root.left)} {self.serialize(root.right)}]"
            elif root.left:
                children = f"[{self.serialize(root.left)}]"
            else:
                children = f"[ {self.serialize(root.right)}]"
            ans += children
            
        #print(ans)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        if "[" not in data:
            return TreeNode(int(data))
        
        l = data.index("[")
        r = data.rindex("]")
        root = TreeNode(int(data[:l]))
        
        children_str = data[l+1:r]
        children = self.helper(children_str)
        if "left" in children:
            root.left = self.deserialize(children["left"])
        if "right" in children:
            root.right = self.deserialize(children["right"])
        
        return root
        
        
        
    def helper(self, s):
        "split the children string"
        d = {}
        if s[0] == " ":  # only right child
            d["right"] = s[1:]
            return d
        
        # find the splitting " " char
        n = len(s)
        stack = 0
        for i in range(n):
            if s[i] == "[":
                stack += 1
            elif s[i] == "]":
                stack -= 1
            elif s[i] == " ":
                if stack == 0:
                    d["left"] = s[:i]
                    d["right"] = s[i+1:]
                    return d
                
        d["left"] = s  # only left child
        return d
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
