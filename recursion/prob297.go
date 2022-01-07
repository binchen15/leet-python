/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import (
    "strconv"
    "strings"
    "fmt"
)

type Codec struct {
    
}

func Constructor() Codec {
    return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    
    if root == nil {
        return ""
    }
    
    ans := strconv.Itoa(root.Val)
    
    if root.Left != nil {
        ans += "[" + this.serialize(root.Left)
        if root.Right != nil {
            ans += " " + this.serialize(root.Right) + "]"
        } else {
            ans += "]"
        }
    } else if root.Right != nil {
        ans += "[ " + this.serialize(root.Right) + "]"
    }
    
    fmt.Println(ans)
    return ans
    
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {    
    
    if len(data) == 0 {
        return nil
    }
    
    if ! strings.Contains(data, "[") {
        num, _ := strconv.Atoi(data)
        root := TreeNode{
            Val: num,
        }
        return &root
    }
    
    l, r := strings.Index(data, "["), strings.LastIndex(data, "]")
    
    num, _ := strconv.Atoi(data[:l])
    root := TreeNode{
        Val: num,
    }
    
    children := helper(data[l+1:r])
    
    left_str, ok := children["left"]
    if ok {
        root.Left = this.deserialize(left_str)
    }
    
    right_str, ok := children["right"]
    if ok {
        root.Right = this.deserialize(right_str)
    }
    
    return &root
    
}

func helper(s string) map[string]string {
    
    ans := map[string]string{}
    
    if s[0] == ' ' {
        ans["right"] = s[1:]
        return ans
    }
    
    stack := 0
    n := len(s)
    for i := 0; i < n; i++ {
        if s[i] == '[' {
            stack++
        } else if s[i] == ']' {
            stack--
        } else if s[i] == ' ' {
            if stack == 0 {
                ans["left"] = s[:i]
                ans["right"] = s[i+1:]
                return ans
            }
        }
    }
    
    ans["left"] = s
    
    return ans
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */

