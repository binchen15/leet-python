type TicTacToe struct {
    n int
    board [][]int
    
}


func Constructor(n int) TicTacToe {
    
    matrix := make([][]int, n)
    for i := 0; i < n; i++ {
        matrix[i] = make([]int, n)
    }
    
    t := TicTacToe{
        n: n,
        board: matrix,
    }
    
    return t
}


func (this *TicTacToe) Move(row int, col int, player int) int {
    
    this.board[row][col] = player
    return helper(this.board, this.n)
    
}

func helper(board [][]int, n int) int {
    
    for i := 0; i < n; i++ {
        val := board[i][i]
        if val != 0 {
            if test_row(i, val, board, n) || test_col(i, val, board, n) {
                return val
            }
        }
    }
    
    if test_diag(board, n, 1) {
        return 1
    }
    
    if test_diag(board, n, 2) {
        return 2
    }
    
    if test_diag2(board, n, 1) {
        return 1
    }
    
    if test_diag2(board, n, 2) {
        return 2
    }
    
    return 0
}

func test_diag(board [][]int, n int, v int) bool {
    for i := 0; i < n; i++ {
        if board[i][i] != v {
            return false
        }
    }
    return true
}

func test_diag2(board [][]int, n int, v int) bool {
    for i := 0; i < n; i++ {
        if board[i][n-i-1] != v {
            return false
        }
    }
    return true
}

func test_row(i int, val int, board [][]int, n int) bool {
    for c:= 0; c< n; c++ {
        if board[i][c] != val {
            return false
        }
    }
    return true
}

func test_col(i int, val int, board [][]int, n int) bool {
    for r := 0; r < n; r++ {
        if board[r][i] != val {
            return false
        }
    }
    return true
}

