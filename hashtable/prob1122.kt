/* 1122 Relative Sort Array*/
class Solution {

    fun relativeSortArray(arr1: IntArray, arr2: IntArray): IntArray {

        val m = mutableMapOf<Int,Int>()
        for (v in arr1) {
            m[v] = m.getOrDefault(v, 0) + 1
        }

        var ans = mutableListOf<Int>()

        for (v in arr2) {
            ans.addAll(List<Int>(m[v]!!) {it -> v})
            m.remove(v)
        }

        val tmp = m.toList().sortedBy {it -> it.first}
        for ((k, v) in tmp) {
            ans.addAll( List(v) {k})
        }

        return ans.toIntArray()

    }
}
