class Solution {
    fun freqAlphabets(s: String): String {
        
        var sb = StringBuilder()
        val n = s.length
        var i = 0
        var tmp: Char
        while (i < n) {
            if (i+2 < n && s[i+2] == '#') {
                tmp = 'a' + s.substring(i..(i+1)).toInt() - 1
                i += 3
            } else {
                tmp = 'a' + s[i].toString().toInt() - 1
                i += 1
            }
            sb.append(tmp)
        }
        
        return sb.toString()
    }
}
