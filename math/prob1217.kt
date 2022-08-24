class Solution {
    
    fun minCostToMoveChips(position: IntArray): Int {
        
        var evn = 0
        var odd = 0
        for (v in position) {
            if (v % 2 == 0) {
                evn++
            } else {
                odd++
            }
        }
        
        return if (evn <= odd) evn else odd
        
    }
}
