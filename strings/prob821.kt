// 821 Shortest Distance to a character

class Solution {
    fun shortestToChar(s: String, c: Char): IntArray {

        // indices storing occurences of char c
        val cs = mutableListOf<Int>()
        for (i in 0 until s.length) {
            if (s[i] == c) cs.add(i)
        }

        // left and right boundary for current char to traverse
        var lb = -1
        var n = s.length
        var ans = IntArray(n)

        for (i in 0 until s.length) {
            var tmp = s[i]
            if (tmp == c) {
                ans[i] = 0
                lb++
            } else {
                if (lb == -1) {
                    ans[i] = cs[0] - i
                } else if (lb < cs.size-1) {
                    ans[i] = Math.min(i-cs[lb], cs[lb+1]-i)
                } else {
                    ans[i] = i-cs[lb]
                }
            }
        }

        return ans

    }
}
