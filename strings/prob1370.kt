// 1370 Increasing/Decreasing String
//
class Solution {
    fun sortString(s: String): String {
        
        val m = mutableMapOf<Char, Int>()
        
        for (c in s) {
            m.put(c, m.getOrDefault(c, 0) + 1)
        }
        
        val sb = StringBuilder()
        
        var inOrder = true
        
        while (m.size > 0) {
            helper(sb, inOrder, m)
            inOrder = !inOrder
        }
        
        return sb.toString()
        
    }
    
    fun helper(sb: StringBuilder, inOrder: Boolean, m: MutableMap<Char, Int>) {
        if (m.size == 0) {
            return
        }
        
        val keys: List<Char>
        
        if (inOrder) {
            keys = m.keys.sorted()
        } else {
            keys = m.keys.sortedDescending()
        } 
        
        for (key in keys) {
            sb.append(key)
            var tmp = m.getOrDefault(key, 0)
            if (tmp == 1) {
                m.remove(key)
            } else {
                m.put(key, tmp-1)
            }
        }
    }
}
