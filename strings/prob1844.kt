class Solution {
    fun replaceDigits(s: String): String {
        
        var tmp = s.toMutableList() // split("")
        for (i in 1 until s.length step 2) {
            tmp[i] = tmp[i-1] + tmp[i].toString().toInt()
        }
        
        return tmp.joinToString("")
    }
}
