class Solution {
    fun frequencySort(nums: IntArray): IntArray {
        
        var m = mutableMapOf<Int, Int>()
        for (v in nums) {
            m[v] = m.getOrDefault(v, 0) + 1
        }
        
        val t = m.toList().sortedWith(compareBy<Pair<Int, Int>> {it-> it.second} .thenByDescending<Pair<Int, Int>> {it->it.first})
        var ans = mutableListOf<Int>()
        for ((k, v) in t) {
            ans.addAll(List(v) {k})
        }
        return ans.toIntArray()
        
    }
}
