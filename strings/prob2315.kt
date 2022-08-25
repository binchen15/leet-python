class Solution {
    fun countAsterisks(s: String): Int {
        
        var flag = true
        var cnts = 0
        
        for (i in 0 until s.length) {
            if (s[i] == '|') {
                if (!flag) {
                    flag = true
                } else if ( '|' in s.substring((i+1) until s.length)) {
                    flag = false
                }
            } else if (s[i] == '*' && flag) {
                cnts++
            }
        }
        
        return cnts
        
    }
}

// slightly better by find last index of '|'
class Solution {
    fun countAsterisks(s: String): Int {
        
        var flag = true
        var cnts = 0
        
        val last = s.lastIndexOf('|')
        if (last == -1) {
            return s.filter {it -> it == '*'} .length
        }
        
        for (i in 0 until s.length) {
            if (s[i] == '|') {
                if (!flag) {
                    flag = true
                } else if (i < last) {
                    flag = false
                }
            } else if (flag && s[i] == '*') {
                cnts++
            }
        }
        
        return cnts
        
    }
}
