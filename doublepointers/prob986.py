# 986 interval list intersecions

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        m = len(firstList)
        n = len(secondList)
        ans = []

        if not m or not n:
            return ans

        i, j = 0, 0 # pointers to first and second list

        while i < m and j < n:
            inter = self.helper(firstList[i], secondList[j])
            if inter:
                ans.append(inter)
            y0 = firstList[i][1]
            y1 = secondList[j][1]

            if y0 == y1:
                i += 1
                j += 1
            elif y0 > y1:
                j += 1
            else:
                i += 1

        return ans

    def helper(self, first, second):
        x0, y0 = first
        x1, y1 = second

        if y0 < x1 or y1 < x0:
            return None
        else:
            return [max(x0, x1), min(y0, y1)]
