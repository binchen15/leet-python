// Maximum 69 Number
class Solution {
    fun maximum69Number (num: Int): Int {
        
        return num.toString().replaceFirst("6", "9").toInt()
        
    }
}
