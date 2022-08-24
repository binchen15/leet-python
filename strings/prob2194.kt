// 2194 Cells in a Range on an Excel Sheet 
class Solution {
    fun cellsInRange(s: String): List<String> {

        var c1 = s[0]
        var r1 = s[1]
        var c2 = s[3]
        var r2 = s[4]

        var ans = mutableListOf<String>()
        for (c in c1..c2) {
            for (r in r1..r2) {
                ans.add("$c$r")
            }
        }

        return ans
    }
}
