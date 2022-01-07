* Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import (
    "strings"
    "strconv"
)

func str2tree(s string) *TreeNode {
    
    if len(s) == 0 {
        return nil
    }
    
    l := strings.Index(s, "(")
    if l == -1 {
        num, _ := strconv.Atoi(s)
        return &TreeNode{
            Val: num,
        }
    }
    
    root_str, left_str, right_str := helper(s)
    
    num2, _ := strconv.Atoi(root_str)
    root := TreeNode {
        Val: num2,
    }
    root.Left = str2tree(left_str)
    root.Right = str2tree(right_str)
    return &root
}

func helper(s string) (string, string, string) {
    
    n := len(s)
    l := strings.Index(s, "(")
    root := s[:l]
    stack := 1
    var r int
    
    for i := l+1; i<n; i++ {
        if s[i] == '(' {
            stack += 1
        } else if s[i] == ')' {
            stack -= 1
            if stack == 0 {
                r = i
                break
            }
        }
    }
    
    left := s[l+1: r]
    var right string
    if r < n-1 {
        right = s[r+2:n-1] 
    } else {
        right = ""
    }
    
    return root, left, right
}
