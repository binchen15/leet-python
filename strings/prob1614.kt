// 1614. Maximum Nesting Depth of the Parentheses

class Solution {
    fun maxDepth(s: String): Int {

        var l = 0
        var ans = 0
        for (c in s) {
            if (c == '(') {
                l++
                if (l > ans) {
                    ans = l
                }
            } else if (c == ')') {
                l--
            }
        }

        return ans

    }
}
