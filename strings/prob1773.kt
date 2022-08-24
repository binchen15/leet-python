// 1773 Count Items matching a rule

class Solution {
    fun countMatches(items: List<List<String>>, ruleKey: String, ruleValue: String): Int {

        val ind = when (ruleKey) {
            "type" -> 0
            "color" -> 1
            else -> 2
        }

        var ans = 0
        for (item in items) {
            if (item[ind] == ruleValue) {
                ans++
            }
        }

        return ans

    }
}
