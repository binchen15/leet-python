// 1684 Count Number of Consistent Strings
//

class Solution {
    fun countConsistentStrings(allowed: String, words: Array<String>): Int {

        var d = allowed.toSet()
        var ans = 0
        for (word in words) {
            var good = true
            for (c in word.toSet()) {
                if (c !in d) {
                    good = false
                    break
                }
            }
            if (good) {
                ans++
            }

        }

        return ans

    }
}
