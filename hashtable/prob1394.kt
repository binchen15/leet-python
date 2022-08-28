/* 1394*/

class Solution {
    fun findLucky(arr: IntArray): Int {

        var m = mutableMapOf<Int, Int>()
        for (v in arr) {
            m[v] = m.getOrDefault(v, 0) + 1
        }

        val tmp = m.filter {it -> it.value == it.key }
        if (tmp.size == 0) {
            return -1
        }

        return tmp.toList().sortedBy{it-> -it.first}[0].first

    }
}
