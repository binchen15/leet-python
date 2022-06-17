class Solution:
    def minTimeToType(self, word: str) -> int:
        
        curr = "a"  # current letter pointed at
        seconds = 0
        
        def dist(c1, c2):
            """calculate distance between two letters on the typerwriter"""
            # n1, n2 = ord(c1)-ord('a'), ord(c2)-ord('a')
            n1, n2 = ord(c1), ord(c2)
            if n1 > n2:
                n1, n2 = n2, n1
            d = min(n2-n1, n1+26-n2)
            return d
        
        for lett in word:
            d = dist(curr, lett)
            seconds += d  # move the pointer
            seconds += 1  # type the letter
            curr = lett   # update the current pointer
            
        return seconds
