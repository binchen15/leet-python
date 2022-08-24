// 1252 Cells with Odd Values in a Matrix
class Solution {
    fun oddCells(m: Int, n: Int, indices: Array<IntArray>): Int {

        var rmap = mutableMapOf<Int, Int>()
        var cmap = mutableMapOf<Int, Int>()

        for ((r, c) in indices) {
            rmap.put(r, rmap.getOrDefault(r, 0) + 1)
            cmap.put(c, cmap.getOrDefault(c, 0) + 1)
        }

        var ans = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
               var tmp = rmap.getOrDefault(r, 0) + cmap.getOrDefault(c, 0)
               ans += if (tmp % 2 == 1) 1 else 0
            }
        }

        return ans

    }
}
