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

// solution 2
type TicTacToe struct {
    n int
    board [][]int
    
}


func Constructor(n int) TicTacToe {
    board := make([][]int, n)
    for i := 0; i < n; i++ {
        board[i] = make([]int, n)
    }
    
    t := TicTacToe {
        n: n,
        board: board,
    }
    
    return t
}


func (this *TicTacToe) Move(row int, col int, player int) int {
    
    this.board[row][col] = player
    
    if this.test_row(row, player) || this.test_col(col, player) {
       return player 
    }
    
    if row == col && this.test_diag(player) {
        return player
    }
    
    if row + col == this.n - 1 && this.test_diag2(player) {
        return player
    }
    
    return 0
    
}

func (this *TicTacToe) test_row(row int, player int) bool {
    for c := 0; c < this.n; c++ {
        if this.board[row][c] != player {
            return false
        }
    }
    return true
}

func (this *TicTacToe) test_col(col int, player int) bool {
    for r := 0; r < this.n; r++ {
        if this.board[r][col] != player {
            return false
        }
    }
    return true
}

func (this *TicTacToe) test_diag(player int) bool {
    for i := 0; i < this.n; i++ {
        if this.board[i][i] != player {
            return false
        }
    }
    return true
}

func (this *TicTacToe) test_diag2(player int) bool {
    n := this.n
    for i := 0; i < n; i++ {
        if this.board[i][n-1-i] != player {
            return false
        }
    }
    return true
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Move(row,col,player);
 */:wq

