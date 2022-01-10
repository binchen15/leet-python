func validTicTacToe(board []string) bool {
    
    xs, os := counts(board)
    if xs < os || xs - os > 1 {
        return false
    }
    
    if xs == os {
        // last move for O
        if somebody_wins(board, byte('X')) {
            return false
        }
    } else {
        // last move for X
        if somebody_wins(board, byte('O')) {
            return false
        }
    }
    
    // other tests?
    
    return true
    
}

func counts(board []string) (int, int) {
    xs := 0
    os := 0
    for r := 0; r < 3; r++ {
        for _, c := range board[r] {
            if c == 'X' {
                xs++
            } else if c == 'O' {
                os++
            }
        }
    }
    
    return xs, os
}

func somebody_wins(board []string, player byte) bool {
    
    var wins bool
    
    for i := 0; i < 3; i++ {
        wins = true
        for j := 0; j < 3; j++ {
            if board[i][j] != player {
                wins = false
                break
            }
        }   
        if wins {
            return true
        }
    }
    
    for c := 0; c < 3; c++ {
        wins = true
        for r := 0; r < 3; r++ {
            if board[r][c] != player {
                wins = false
                break
            }
        }   
        if wins {
            return true
        }
    }
    
    if board[0][0] == player && board[1][1] == player && board[2][2] == player {
        return true
    }
    
    if board[0][2] == player && board[1][1] == player && board[2][0] == player {
        return true
    }
    
    return false
}
