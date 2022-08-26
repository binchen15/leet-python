class Solution {
    fun kthDistinct(arr: Array<String>, k: Int): String {
        
        var m = mutableMapOf<String, Int>()
        val s = mutableSetOf<String>()
        
        for (i in 0 until arr.size) {
            val word = arr[i]
            if (word in m) {
                s.add(word)
            } else {
                m.put(word, i)
            }
        }
        
        var m2 = m.filter { it -> it.key !in s}
        
        if (m2.size < k) {
            return ""
        }
        
        return m2.toList().sortedBy { (_, value) ->  value} .map { (key, _) ->  key} [k-1]
        
        
    }
}
