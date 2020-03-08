class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        ret = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(len(ret[i-1])-1):
                row.append(ret[i-1][j] + ret[i-1][j+1])
            row.append(1)
            ret.append(row)
        return ret
        
