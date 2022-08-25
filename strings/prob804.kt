// 804 Unique Morse Code Words
//

class Solution {
    fun uniqueMorseRepresentations(words: Array<String>): Int {

        var code = listOf(".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")

        var s = words.toSet()
        var ans = mutableSetOf<String>()
        for (w in s) {
            var sb = StringBuilder()
            for (c in w) {
                sb.append(code[c - 'a'])
            }
            ans.add(sb.toString())
        }

        return ans.size
    }
}
