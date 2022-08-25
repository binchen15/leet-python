// 2325 Decode the message
//
class Solution {
    fun decodeMessage(key: String, message: String): String {
        
        var s = mutableSetOf<Char>()
        var order = mutableListOf<Char>()
        
        for (c in key) {
            if (c in s) {
                continue
            } else if ( 'a' <= c && c <= 'z') {
                s.add(c)
                order.add(c)
                if (order.size == 26) {
                    break
                }
            }
        }
        
        var m = mutableMapOf<Char, Char>()
        for ( (i, c) in order.withIndex() ) {
            m.put(c, 'a'+i)
        }
        
        
        var tmp = mutableListOf<Char>()
        for (c in message) {
            tmp.add(m.getOrDefault(c, ' '))
        }
        
        return tmp.joinToString("")
        
        
    }
}
