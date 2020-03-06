class Solution(object):
    """use python sets, 50% percentile solution"""
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sets = [set(word) for word in words]
        prod = 0
        m    = len(sets)
        for i in range(m-1):
            for j in range(i+1, m):
                if not sets[i].isdisjoint(sets[j]):
                    continue
                else:
                    p  = len(words[i]) * len(words[j])
                    if p > prod:
                        prod = p
        return prod
            
class Solution(object):
    """each word represent by an int. 
		first 26 bits mean each letter exits or not"""
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sets = [set(word) for word in words]
        bits = []
        for s in sets:
            b = 0
            for c in s:
                b  |= 1 << (ord(c) - ord('a'))
            bits.append(b)
        
        prod = 0
        m    = len(sets)
        for i in range(m-1):
            for j in range(i+1, m):
                if bits[i] & bits[j] == 0 :
                    p  = len(words[i]) * len(words[j])
                    if p > prod:
                        prod = p
        return prod
            
         
