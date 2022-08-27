// 2363 Merge Similar Items
//
class Solution {
    fun mergeSimilarItems(items1: Array<IntArray>, items2: Array<IntArray>): List<List<Int>> {
        
        val s2 = mutableMapOf<Int, Int>()
        val s = mutableMapOf<Int, Int>()
        
        for ( (v, w) in items2 ) {
            s2[v] = w
        }
        
        for ((v, w) in items1) {
            s[v] = w + s2.getOrDefault(v, 0)
        }
        
        for ((v, w) in s2.entries){
            if (v !in s) {
                s[v] = w
            }
        }
    
        return s.toList().sortedBy{it.first}.map{ it.toList() }
        
    }
}
