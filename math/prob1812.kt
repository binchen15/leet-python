class Solution {
    fun squareIsWhite(coordinates: String): Boolean {
        
        val c = coordinates[0]
        val r = coordinates[1]
        val l = (c - 'a') + (r - '1')
        
        return l % 2 == 1
        
    }
}
