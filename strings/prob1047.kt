// timelimit error

class Solution {

    fun removeDuplicates(s: String): String {
        val n = s.length
        if (n <= 1) {
            return s
        }
        var i = 0
        while (i < n-1) {
            if (s[i] == s[i+1]) {
                var tmp = s.substring(0 until i) + s.substring((i+2) until n)
                return removeDuplicates(tmp)
            } else {
                i++
            }
        }
        return s

    }
}

# timelimit again
class Solution {

    fun removeDuplicates(s: String): String {

        var t = s
        var n = t.length
        if (n <= 1) {
            return t
        }
        var i = 0
        while (i < n-1) {
            if (t[i] == t[i+1]) {
                t = t.substring(0 until i) + t.substring((i+2) until n)
                n -= 2
                if (i >= 1) {
                    i--
                }
            } else {
                i++
            }
        }
        return t

    }
}

class Solution {
    
    fun removeDuplicates(s: String): String {

        var l = mutableListOf<Char>()
        val n = s.length
        var i = 0
        while (i < n) {
            var c = s[i]
            if (l.size == 0) {
                l.add(c)
            } else {
               if (l.last() != c) {
                   l.add(c)
               }  else {
                   l.removeAt(l.size-1)
               }
            }
            i++
        }
        
        return l.joinToString("")
    }
        
}
