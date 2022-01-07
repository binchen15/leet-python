"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            ans = ""
        else:
            if not root.children:
                ans = f"{root.val}"
            else:
                children = [self.serialize(child) for child in root.children if child]
                children_str = " ".join(children)
                ans = f"{root.val}[{children_str}]"        
        return ans
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        if "[" not in data:
            return Node(int(data), [])
        
        l = data.index("[")
        r = data.rindex("]")
        root = Node(int(data[:l]), [])
        children_str = data[l+1:r]
        if children_str:
            children_list = self.helper(children_str)
            children = [ self.deserialize(child_str) for child_str in children_list]
            root.children = children
        
        return root
        

    def helper(self, s):
        "partition s into a list of children"
        n = len(s)
        ans = []
        if not n:
            return ans
        stack = 0
        for i in range(n):
            if s[i] == "[":
                stack += 1
            elif s[i] == "]":
                stack -= 1
            elif s[i] == " ":
                if stack == 0:
                    ans.append(s[:i])
                    others = self.helper(s[i+1:])
                    ans.extend(others)
                    return ans
                    
        return [s]

