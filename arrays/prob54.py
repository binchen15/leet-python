#spiral matrix
# note: 1st and last row, 1 and last col might coincide.
# so need handle edge cases carefully.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        ans = []

        for j in range(n):
            ans.append(matrix[0][j])
        for i in range(1, m):
            ans.append(matrix[i][n-1])
        if m >= 2:
            for j in range(n-2, -1, -1):
                ans.append(matrix[m-1][j])
        if n >= 2:
            for i in range(m-2, 0, -1):
                ans.append(matrix[i][0])

        m2 = []  # smaller problem for recursion
        for r in range(1, m-1):  # m-2 rows, n-2 cols
            m2.append(matrix[r][1:-1])

        # print(ans, m2)

        ans += self.spiralOrder(m2)

        return ans

