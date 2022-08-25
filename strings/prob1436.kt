class Solution {
    fun destCity(paths: List<List<String>>): String {
        
        var starts = mutableSetOf<String>()
        var ends = mutableSetOf<String>()
        for ( (start, end) in paths) {
            starts.add(start)
            ends.add(end)
        }
        
        for (end in ends) {
            if (end !in starts) {
                return end
            }
        }
        
        throw Exception("Should not happen")
        
    }
}

class Solution {
    fun destCity(paths: List<List<String>>): String {

        var starts = mutableSetOf<String>()
        var ends = mutableSetOf<String>()
        for ( (start, end) in paths) {
            starts.add(start)
            ends.add(end)
        }

        return (ends subtract starts).toList()[0]
        // throw Exception("Should not happen")

    }
}
