# partition labels
# took like 2.5 hours... 

class Solution(object):

    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        chars = set(S)
        p = [ [S.index(c), S.rindex(c)] for c in chars]

        # how to merge them??
        cards = sorted(p, key=lambda x : x[0])
        m = len(cards)
        if m == 1:
            return [len(S)]

        i = 0       # first card
        parts = []  # merged partitions
        while i < m:
            card = cards[i]
            j = i+1
            while j < m:
                after = cards[j]
                if after[0] <= card[1]:  # intersect
                    card = self.merge(card, after)
                    j += 1
                else:  # non-overlapping
                    #parts.append(card)
                    #i = j
                    break
            parts.append(card)
            i = j
        parts.sort(key= lambda x : x[0]) # should not need it
        ans = [ p[1] - p[0] + 1 for p in parts]
        return ans

    def merge(self, card1, card2):
        """this assumes card1 intersects card2"""
        return [ min(card1[0], card2[0]), max(card1[1], card2[1]) ]




