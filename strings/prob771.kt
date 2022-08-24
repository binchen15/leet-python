class Solution {
    fun numJewelsInStones(jewels: String, stones: String): Int {
        
        val js = jewels.toSet()
        var ans = 0
        for (c in stones) {
            if (c in js) {
                ans++
            }
        }
        
        return ans
    }
}
