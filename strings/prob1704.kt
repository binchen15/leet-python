// 5%
class Solution {
    fun halvesAreAlike(s: String): Boolean {
        // var t = s.toLowerCase()
        val n = s.length / 2
        var l = s.substring(0 until n)
        var r = s.substring(n until (2*n))
        
        val vowels = setOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        return l.filter({i -> i in vowels}).length == r.filter({i -> i in vowels}).length
        
    }
}

// 25%
class Solution {
    fun halvesAreAlike(s: String): Boolean {
        // var t = s.toLowerCase()
        val n = s.length / 2
        var l = s.substring(0 until n)
        var r = s.substring(n until (2*n))        
        val vowels = setOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        return l.count({i -> i in vowels}) == r.count({i -> i in vowels})
        
    }
}

