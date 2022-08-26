// 1002 Find Common Characters

class Solution {
    fun commonChars(words: Array<String>): List<String> {

        val l = mutableListOf<MutableMap<Char, Int>>()

        for (word in words) {
            l.add(helper(word))
        }

        val n = words.size

        if (n == 1) {
            return words[0].toList().map {it -> it.toString()}
        }

        val ans = mutableListOf<String>()

        for (c in words[0]) {
            var flag = true
            for (i in 1 until n) {
                var tmp = l[i]
                if (c !in tmp) {
                    flag = false
                    break
                } else {
                    var cnt = tmp.getOrDefault(c, 0)
                    if (cnt == 1) {
                        tmp.remove(c)
                    } else {
                        tmp.put(c, cnt-1)
                    }
                }
            }
            if (flag) {
                ans.add(c.toString())
            }

        }

        return ans
    }

    fun helper(word: String): MutableMap<Char, Int> {
        var m = mutableMapOf<Char, Int>()
        for (c in word) {
            m.put(c, m.getOrDefault(c, 0)+1)
        }
        return m
    }
}
