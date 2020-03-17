# 127 word ladder

# time limit error
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        m     = len(wordList)
        currL = [beginWord]
        nextL = []
        level = 0
        marked = [False] * m
        while currL:
            level += 1
            while currL:
                word = currL.pop(0)
                if word == endWord:
                    return level
                for i in range(m):
                    if not marked[i] and self.candidate(word, wordList[i]):
                        nextL.append(wordList[i])
                        marked[i] = True
            currL = nextL
            nextL = []
        return 0

    def candidate(self, s, t):
        """does two word differ by exactly one char"""
        flag = False
        for i in range(len(s)):
            if s[i] != t[i]:
                if flag:
                    return False # more than one char differs
                else:
                    flag = True
        return flag

# build graph first. time limit error
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        start = wordList.index(beginWord)
        end   = wordList.index(endWord)
        
        graph  = self.buildGraph(wordList)
        if not graph[start] or not graph[end]:
            return 0
        currL = [start]
        nextL = []
        level = 0
        marked = [False] * len(wordList)
        marked[start] = True
        while currL:
            level += 1
            while currL:
                i = currL.pop(0)
                if i == end:
                    return level
                else:
                    for j in graph[i]:
                        if not marked[j]:
                            nextL.append(j)
                            marked[j] = True   
            currL = nextL
            nextL = []
        return 0
        
    
    def buildGraph(self, wordList):
        graph = {} # dict of list of indices
        L  = len(wordList[0])  # all words same length
        m  = len(wordList)
        for i in range(m):
            row = set()
            for j in range(m):
                if j != i and self.connected(wordList[i], wordList[j], L):
                    row.add(j)  # i->j
            graph[i]=row
        return graph
            
                               
    def connected(self, s, t, L):
        """does wordList[i], wordList[j] connect?"""
        cnt = 0
        for i in range(L):
            if s[i] != t[i]:
                if cnt == 1:
                    return False
                else:
                    cnt = 1
        return cnt == 1



# 40% solution
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set(wordList)
        if endWord not in words:
            return 0

        currL = [beginWord]
        nextL = []
        level = 0
        while currL:
            level += 1
            while currL:
                word = currL.pop(0)
                if word == endWord:
                    return level
                for nb in self.findNeighbors(word, words):
                    nextL.append(nb)
            currL = nextL
            nextL = []
        return 0

    def findNeighbors(self, word, words):
        ans = set()
        for i, _ in enumerate(word):
            for c in string.ascii_lowercase:
                cand = word[:i] + c + word[i+1:]
                if cand in words:
                    ans.add(cand)
                    words.remove(cand)
        return ans


