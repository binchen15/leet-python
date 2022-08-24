class Solution {
    fun interpret(command: String): String {
        return command.replace("(al)", "al").replace("()","o")   
    }
}
