class Solution {
    fun mostWordsFound(sentences: Array<String>): Int {
        return sentences.map({it-> it.split(" ").size}).max()!!
    }
}

class Solution {
    fun mostWordsFound(sentences: Array<String>): Int {
        return sentences.map({it-> it.split(" ").size}).max() ?: 0
    }
}
