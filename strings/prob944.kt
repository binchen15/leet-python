// 944. Delete Columns to make sorted

class Solution {
    fun minDeletionSize(strs: Array<String>): Int {

        val rs = strs.size
        if (rs <= 1) return 0

        val cs = strs[0].length
        if (cs == 0) return 0

        var cnts = 0
        for (c in 0 until cs) {
            var flag = true
            for (r in 1 until rs) {
                if (strs[r][c] < strs[r-1][c] ) {
                    flag = false
                    break
                }
            }
            if (!flag) cnts++
        }

        return cnts

    }
}
