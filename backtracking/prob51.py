# N queens problem

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        positions = [-1] * n
        ans = []
        def show():
            board = [ ["."] * n for _ in range(n)]
            for row, col in enumerate(positions):
                board[row][col] = "Q"
            llist = [ "".join(row)  for row in board]
            ans.append(llist)

        def check(k):
            if k == 0:
                return True
            for i in range(k):
                if positions[k] == positions[i]:
                    return False
                if abs(positions[k] - positions[i]) == abs(k - i):
                    return False
            return True


        def backtrack(k):
            """place the k-th queeen"""

            if k == n:
                show()
                return

            for i in range(n):
                positions[k] = i
                if check(k):
                    backtrack(k+1)
                positions[k] = -1

        backtrack(0)
        return ans
