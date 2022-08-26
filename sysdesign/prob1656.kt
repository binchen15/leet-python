// 1656 Design an Ordered Stream
class OrderedStream(n: Int) {

    var ptr = 0 // the next one to output
    var data: Array<String>
    val n: Int = n
    init {
        data = Array<String>(n, {it-> ""})
    }
    
    fun insert(idKey: Int, value: String): List<String> {
        val tmp = idKey-1
        data[tmp] = value
        if (tmp != ptr) {
            return listOf<String>()
        } else {
            val ans = mutableListOf<String>()
            while (ptr < n && data[ptr] != "") {
                ans.add(data[ptr])
                ptr++
            }
            return ans
        }
    }

}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
