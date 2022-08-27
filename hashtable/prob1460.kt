class Solution {
    fun canBeEqual(target: IntArray, arr: IntArray): Boolean {
        
        var m1 = mutableMapOf<Int, Int>()
        var m2 = mutableMapOf<Int, Int>()
        
        for (v in target) {
            m1[v] = m1.getOrDefault(v, 0) + 1
        }
        
        for (v in arr) {
            m2[v] = m2.getOrDefault(v, 0) + 1
        }
        
        return m1 == m2
    }
}
