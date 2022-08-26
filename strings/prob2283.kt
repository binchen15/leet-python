class Solution {
    fun digitCount(num: String): Boolean {
        var m = mutableMapOf<Char, Int>()
        for (c in num) {
            m.put(c, m.getOrDefault(c, 0)+1)
        }
        
        val n = num.length
        //println(m)
        for (i in 0 until n) {
            if (m.getOrDefault(i.toString()[0], 0) != num[i].toString().toInt())  {
                return false
            }
        }
        
        return true
    }
}
