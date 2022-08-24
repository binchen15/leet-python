// 728 Brute force 5% solution
class Solution {
    fun selfDividingNumbers(left: Int, right: Int): List<Int> {
        
        val ans = mutableListOf<Int>()
        for (v in left..right) {
            if (helper(v)){
                ans.add(v)
            }
        }
    
        return ans
    }
    
    fun helper(n: Int): Boolean {
        var s = n.toString().toList().toSet().map {it-> it.toString().toInt()}
        if (0 in s) {
            return false
        } else {
            for (d in s) {
                if (n % d != 0) {
                    return false
                }
            }
            return true
        }
    }

}
