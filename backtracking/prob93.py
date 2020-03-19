#93 restore IP address

# your own ugly solution withour reference any help
# 50%
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = len(s)
        if m < 4:
            return []
        
        tree = {}
        self.buildTree(s, tree, m, 0, 0)
        self.trimTree(tree, 4)
        ans = self.walkTree(tree)
        ret = filter(lambda x: len(x) == m + 3, ans)
        return ret
        
    def buildTree(self, s, node, m, start, level):
        """level [0,3], s[start:] """
        if start >= m or level > 3:
            return
        if level == 3:  # last level
            key = s[start:]
            if len(key) > 3 or int(key) > 255 or \
                (key.startswith('0') and len(key) > 1):
                return
            else:
                node[key] = {}
                return
        for i in range(1,4):
            end = start + i
            if end <= m:
                key = s[start:end]
                if int(key) <= 255 and \
                   not (key.startswith('0') and len(key) > 1):
                    node[key] = {}
        for key in node:
            self.buildTree(s, node[key], m, start+len(key), level+1)
            
    def depth(self, tree):
        if not tree:
            return 0
        subs = [self.depth(tree[key]) for key in tree ]
        return 1 + max(subs)
    
    def trimTree(self, node, level):
        """node must be of depth level"""
        if self.depth(node) != level:
            del node
            return
        for key in node:
            self.trimTree(node[key], level-1)
            
    def walkTree(self, node):
        if not node:  # the last level 
            return [""]
        ans = []
        for key in node:
            ls = self.walkTree(node[key])
            for s in ls:
                if s:
                    ans.append("{}.{}".format(key, s))
                else:
                    ans.append(key)
        return ans
           
# slightly better. Trim tree along the way. 80% solution

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = len(s)
        if m < 4:
            return []
        
        tree = {}
        flag = self.buildTree(s, tree, m, 0, 0)
        if not flag:
            return []
        return self.walkTree(tree)

    def buildTree(self, s, node, m, start, level):
        """level [0,3], s[start:] """
        if start >= m or level > 3:
            return False
        if level == 3:  # last level
            key = s[start:]
            if len(key) > 3 or int(key) > 255 or \
                (key.startswith('0') and len(key) > 1):
                return False
            else:
                node[key] = {}
                return True
        for i in range(1,4):
            end = start + i
            if end <= m:
                key = s[start:end]
                if int(key) <= 255 and \
                   not (key.startswith('0') and len(key) > 1):
                    node[key] = {}
        bk = []  # failed/bad keys
        for key in node:
            flag = self.buildTree(s, node[key], m, start+len(key), level+1)
            if not flag:
                bk.append(key)
        for key in bk:
            del node[key]
        if not node:
            return False
        else:
            return True
                        
    def walkTree(self, node):
        if not node:  # the last level 
            return [""]
        ans = []
        for key in node:
            ls = self.walkTree(node[key])
            for s in ls:
                if s:
                    ans.append("{}.{}".format(key, s))
                else:
                    ans.append(key)
        return ans
