class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        ans =  [[1], [1,1]]
        for row in range(2, numRows):
            prev = ans[row-1]
            cur = [1]
            for i in range(len(prev)-1):
                cur.append(prev[i]+prev[i+1])
            cur.append(1)
            ans.append(cur)
        return ans

