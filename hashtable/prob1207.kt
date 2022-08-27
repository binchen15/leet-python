class Solution {
    fun uniqueOccurrences(arr: IntArray): Boolean {
        
        var m = mutableMapOf<Int, Int>()
        for (v in arr) {
            m[v] = m.getOrDefault(v, 0) + 1
        }
        
        var t = m.values
        return t.size == t.toSet().size
        
    }
}
