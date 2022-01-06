class Solution:
    def reorganizeString(self, s: str) -> str:
        
        from collections import Counter
        import heapq
        
        class Char:
            def __init__(self, char, cnt):
                self.char = char
                self.cnt = cnt
                
            def __lt__(self, other):
                return self.cnt > other.cnt
        
        d = Counter(s)
        n = len(s)
        
        h = [Char(k, v) for k, v in d.items()]
        heapq.heapify(h)
        
        s = ""
        while h:
            if len(h) >= 2:
                o1 = heapq.heappop(h)
                o2 = heapq.heappop(h)
                c1 = o1.char
                c2 = o2.char
                s = s + (c1 + c2)
                d[c1] -= 1
                d[c2] -= 1
                if d[c1] > 0:
                    heapq.heappush(h, Char(c1, d[c1]))
                if d[c2] > 0:
                    heapq.heappush(h, Char(c2, d[c2]))
            else:
                o = heapq.heappop(h)
                if o.cnt == 1:
                    s += o.char
                    return s
                else:
                    return ""
        
        return s

