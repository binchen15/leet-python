# top K frequent words

# this does not use heap
class Solution(object):
    """83%"""
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wc = {}   # word count
        for w in words:
            wc[w] = wc.get(w, 0) + 1
          
				# sorting words by alphabeta
        sw = sorted(wc.keys())
        lc = { w:i for i, w in enumerate(sw)}
        scale = 10  # weighting offset, frequency dominate the alphabeta
        while scale <= len(sw):
            scale *= 10
        
        data = sorted(wc.items(), 
                      key=lambda x : -x[1] * scale + lc[x[0]] )
        ws = [ p[0] for p in data]
        return ws[:k]

class Solution(object):
    """60%"""
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wc = {}
        for w in words:
            wc[w] = wc.get(w, 0) + 1
            
        class WordCount:            
            def __init__(self, word, count):
                self.word  = word
                self.count = count
            
            def __eq__(self, other):
                return  self.word  == other.word and \
                        self.count == other.count
            
            def __lt__(self, other):
                if self.count < other.count:
                    return True
                elif self.count > other.count:
                    return False
                else:
                    return self.word > other.word
            
                  
        objs = [ WordCount(w, wc[w]) for w in wc]
        import heapq
        data = heapq.nlargest(k, objs)
        return [ obj.word for obj in data]
                

class Solution(object):
    """60% solution"""
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wc = {}
        for w in words:
            wc[w] = wc.get(w, 0) + 1
            
        class WordCount:            
            def __init__(self, word, count):
                self.word  = word
                self.count = count
            
            def __eq__(self, other):
                return  self.word  == other.word and \
                        self.count == other.count
            
            def __lt__(self, other):
                if self.count < other.count:
                    return True
                elif self.count > other.count:
                    return False
                else:
                    return self.word > other.word
            
        import heapq
        objs = []   # min heap
        for w in wc:
            obj = WordCount(w, wc[w])
            if len(objs) < k:
                heapq.heappush(objs, obj)
            elif obj > objs[0]:
                heapq.heapreplace(objs, obj)
                
        words = []
        for i in range(k):
            words.insert(0, heapq.heappop(objs).word)
        return words
    
                
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        cnts = {}
        for word in words:
            cnts[word] = cnts.get(word, 0) + 1
            
        tmp = sorted(cnts.items(), key = lambda x: (-x[1], x[0]))[:k]
        ans = [item[0] for item in tmp]
        return ans
